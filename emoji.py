def emoji_function(input_name):
        split = input_name.split(' ')
        emoji_dictionary_creation = {
          ':)': '😀',
          ':(': '🙃',
          ":D": "😎",
          ":P": "🤪",
          ":L": "🥰"
        }
        output = ''
        for CH in split:
            output += emoji_dictionary_creation.get(CH, CH) + ' '
        return output


input_name = input('<< ')
result = emoji_function(input_name)
print(result)