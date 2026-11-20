from translate import Translator
a = int(input("中文翻译1，英文翻译0："))
c = input("请输入：")
if int((a >= 1)):

    translator= Translator(to_lang="chinese")
    translation = translator.translate(c)

else:

    translator = Translator(to_lang="english")
    translation = translator.translate(c)
print("翻译：", translation)

'''from translate import Translator
translator= Translator(to_lang="chinese")#指定要翻译成的语言
translation = translator.translate("Good night!")
print(translation)
'''



