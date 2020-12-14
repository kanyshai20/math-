import sys

formulas = []
with open('formulas.txt', mode='r', encoding="utf-8") as file:
    readfile = file.readlines()
    for f in readfile:
        formulas.append(f)

isExit = True
while isExit:
    user_input = input('Please Enter Geometrical Keyword whose formula you want? ')
    results = []
    isFound = False
    for i in range(len(formulas)):
        user_input = str(user_input).lower()
        line = (str(formulas[i]).lower()).split(',')
        if 'exit' in user_input or 'quit' in user_input:
            sys.exit(0)
        if (line[0] in user_input) and (line[1] in user_input):
            if len(line)<=1:
                print('1')
                results.append('Formula for '+ line[0].title()+ ' is: '+ line[1])
            else:
                results.append('Formula for '+ line[0].title()+' of '+line[1].title()+ ' is: '+ line[2])
            isFound = True
        elif user_input in line[0]:
            if len(line)<=2:
                results.append('Formula for '+line[0].title()+' is: '+line[1])
            else:
                results.append('Formula for '+line[0].title()+' of '+line[1].title()+ ' is: '+line[2])
            # print(str(formulas[i]))
            isFound = True
        elif user_input in line[1]:
            # print('Please Enter what you want of ', line[1])
            if len(line)<=2:
                results.append('Formula for '+ line[0].title()+ ' is: '+ line[1])
            else:
                results.append('Formula for '+ line[0].title()+' of '+line[1].title()+ ' is: '+ line[2])
            # print(str(formulas[i]))
            isFound = True
    if not isFound:
        print("Sorry, I dont know the formula of", user_input)
        value = input('Press V to store its formula, or Press any other character to escape: ')
        if value[0].lower()=='v':
            value = input('Enter formula for '+ user_input+": ")
            try:
                f = open("formulas.txt", "a")
                f.write('\n'+user_input + ', ' + value)
                f.close()

                formulas = []
                formulas.clear()
                with open('formulas.txt', mode='r', encoding="utf-8") as file:
                    readfile = file.readlines()
                    for f in readfile:
                        formulas.append(f)
                print('Thanks for Saving!!!')
             except:
                print('Sorry, Cannot be saved')

    elif len(results)>1:
        print("####- I HAVE FOUND MORE THAN 1 RESULTS, PLEASE ENTER SPECIFIC ONE -#### ")
        for j in range(len(results)):
            print(results[j].strip())
    elif len(results) == 1:
        print(results[0])
    print('__________________________________________________')
    results.clear()
