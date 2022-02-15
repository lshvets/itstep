text = 'The Star Wars franchise depicts the adventures of characters'
word_list = ['Star', 'Wars']
text_list = text.split(' ')
for i in range(len(word_list)):
    for j in range(len(text_list)):
        if word_list[i].lower() in text_list[j].lower():
            text_list[j] = text_list[j].upper()
upper_text = ''
for text_word in text_list:
    upper_text = upper_text + ' ' + text_word
print(upper_text)
