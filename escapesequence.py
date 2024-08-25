# \\	Backslash (\)
# \'	Single quote (')
# \"	Double quote (")
# \n	Newline (Line break)
# \t	Horizontal tab
# \r	Carriage return
# \b	Backspace
# \f	Form feed (advances to the next "page" in printing)
# \v	Vertical tab
# \a	ASCII bell (makes a beep sound)
# \0	Null character (\x00)
# \N{name}	Unicode character by name (e.g., \N{LATIN SMALL LETTER A})
# \uxxxx	Unicode character with 16-bit hex value (\u263A for ☺)
# \Uxxxxxxxx	Unicode character with 32-bit hex value (\U0001F600 for 😀)
# \ooo	Character with octal value (\141 for a)
# \xhh	Character with hex value (\x61 for a)

print("Hello,\nWorld!") #newline
print("Hello,\tWorld!") #tab
print('It\'s a beautiful day!') #single quote
print("This is a backslash: \\") #back slash
print("Smiley face: \u263A") #unicode
print("Grinning face: \U0001F600") #unicode
