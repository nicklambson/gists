locales = ['en_US', 'zh_CN', 'es_ES', 'es_LA', 'ru', 'de']

print(f"Iterating through locales: {locales}")
print()

print("Using break in a loop")
for locale in locales:
    if locale == 'es_ES':
        print("Found es_ES, breaking loop.")
        break
    print("Locale is", locale)
else:
    print("Did not find es_ES.")

print()

print("Using else after a for loop")
for locale in locales:
    if locale == 'pt_BR':
        print("Found pt_BR, breaking loop.")
        break
    print("Locale is", locale)
else:
    print("Did not find pt_BR.")

print()

print("Using continue in a loop")
for locale in locales:
    if locale == 'es_ES':
        print("Found es_ES, continuing.")
        continue
    print("Locale is", locale)

print()
    
