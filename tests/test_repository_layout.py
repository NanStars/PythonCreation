"""Static-only migration checks. Never import or execute historical programs."""
from pathlib import Path
import ast
import hashlib
import json
import re
import unittest
from urllib.parse import unquote, urlsplit
import posixpath
import csv

ROOT = Path(__file__).resolve().parents[1]

def text_of(path):
    data = path.read_bytes()
    for encoding in ['utf-8', 'gb18030']:
        try: return data.decode(encoding)
        except UnicodeDecodeError: pass
    return None

def local_refs(path, text, paths):
    values = []
    if path.endswith(('.html', '.htm')):
        values += re.findall(r'(?:src|href)\s*=\s*["\']([^"\']+)["\']', text)
    if path.endswith('.css'):
        values += re.findall(r'url\(\s*["\']?([^\s\)"\']+)', text)
    if path.endswith(('.py', '.spec')):
        try: values += [n.value for n in ast.walk(ast.parse(text)) if isinstance(n, ast.Constant) and isinstance(n.value, str)]
        except SyntaxError: pass
    refs = []
    for value in values:
        if not value or value.startswith(('http:', 'https:', '//', 'data:', '#')) or ':' in value: continue
        part = unquote(urlsplit(value).path).replace('\\', '/')
        target = posixpath.normpath(posixpath.join(posixpath.dirname(path), part))
        if target in paths: refs.append(target)
    return set(refs)

def shape(value):
    if isinstance(value, ast.Constant) and isinstance(value.value, str): return {'type': 'Constant', 'string': True}
    if isinstance(value, ast.AST):
        fields = {}
        for key, item in ast.iter_fields(value):
            if key == 'type_params' and not item: continue
            if isinstance(value, ast.Name) and key == 'id' and item == 'sqldata': item = 'database'
            if isinstance(value, ast.alias) and key == 'name' and item == 'sqldata': item = 'database'
            fields[key] = shape(item)
        return {'type': type(value).__name__, 'fields': fields}
    if isinstance(value, list): return [shape(v) for v in value]
    return value

class NamingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = json.loads((ROOT / 'docs/rename-map.json').read_text(encoding='utf-8'))

    def test_every_original_file_has_a_destination(self):
        missing = [e['new'] for e in self.plan['entries'] if not (ROOT / e['new']).is_file()]
        self.assertEqual(missing, [], f'{len(missing)} normalized destinations are missing')

    def test_targets_are_unique_on_windows(self):
        targets = [e['new'].casefold() for e in self.plan['entries']]
        self.assertEqual(len(targets), len(set(targets)))

    def test_paths_are_ascii_and_python_names_are_snake_case(self):
        for entry in self.plan['entries']:
            path = entry['new']
            self.assertTrue(path.isascii(), path)
            self.assertNotIn(' ', path)
            if path.endswith('.py'):
                self.assertRegex(Path(path).name, r'^[a-z][a-z0-9_]*\.py$')

    def test_python_structure_is_preserved(self):
        for entry in self.plan['entries']:
            if not entry['new'].endswith('.py'): continue
            with self.subTest(path=entry['new']):
                data = (ROOT / entry['new']).read_bytes()
                try: tree = ast.parse(data)
                except SyntaxError as error:
                    self.assertEqual(error.msg, entry.get('existing_syntax_error')); continue
                digest = hashlib.sha256(json.dumps(shape(tree), ensure_ascii=False, sort_keys=True).encode()).hexdigest()
                self.assertEqual(digest, entry.get('ast_shape_sha256'))

    def test_binary_and_data_contents_are_preserved(self):
        for entry in self.plan['entries']:
            if Path(entry['new']).suffix.lower() in {'.exe', '.png', '.jpg', '.jpeg', '.ico', '.txt'}:
                digest = hashlib.sha256((ROOT / entry['new']).read_bytes()).hexdigest()
                self.assertEqual(digest, entry['original_sha256'], entry['new'])

    def test_dashboard_local_module_and_template(self):
        root = ROOT / 'data-visualization/epidemic-dashboard'
        source = (root / 'app.py').read_text(encoding='utf-8')
        self.assertIn('import database', source)
        self.assertNotIn('sqldata', source)
        self.assertTrue((root / 'database.py').is_file())
        for template in re.findall(r'render_template\([\'"]([^\'"]+)', source):
            self.assertTrue((root / 'templates' / template).is_file(), template)

    def test_known_existing_local_references_are_preserved(self):
        paths = {e['new'] for e in self.plan['entries']}
        for check in self.plan['local_reference_checks']:
            text = text_of(ROOT / check['source'])
            self.assertTrue(set(check['targets']).issubset(local_refs(check['source'], text, paths)), check['source'])

    def test_remote_urls_were_not_changed(self):
        for entry in self.plan['entries']:
            if 'original_remote_urls_sha256' not in entry: continue
            text = text_of(ROOT / entry['new'])
            urls = re.findall(r'https?://[^\s"\'<>]+', text)
            digest = hashlib.sha256(json.dumps(urls, ensure_ascii=False).encode()).hexdigest()
            self.assertEqual(digest, entry['original_remote_urls_sha256'], entry['new'])

    def test_readme_links_target_real_files_or_directories(self):
        for name in ['README.md', 'README.en.md']:
            text = text_of(ROOT / name)
            for groups in re.findall(r'\]\(([^)]+)\)|src="([^"]+)"', text):
                link = next(x for x in groups if x)
                if link.startswith(('https://', 'http://', '#')): continue
                target = (ROOT / unquote(link)).resolve()
                self.assertTrue(target.is_relative_to(ROOT) and target.exists(), (name, link))

    def test_csv_matches_the_complete_migration_manifest(self):
        with (ROOT / 'docs/path-migration.csv').open(encoding='utf-8', newline='') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual([(r['old_path'], r['new_path']) for r in rows], [(e['old'], e['new']) for e in self.plan['entries']])

    def test_conventional_tool_names_are_the_only_case_exceptions(self):
        special_files = {'README.md', 'README.en.md', '.gitignore', 'Project_Default.xml', 'dataSources.xml'}
        for entry in self.plan['entries']:
            path = Path(entry['new'])
            for part in path.parts[:-1]:
                if part not in {'.idea', 'inspectionProfiles'}:
                    self.assertRegex(part, r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
            if path.name not in special_files:
                self.assertEqual(path.name, path.name.lower())

if __name__ == '__main__':
    unittest.main()
