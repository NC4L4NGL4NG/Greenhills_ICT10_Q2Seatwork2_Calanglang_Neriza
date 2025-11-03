from pyscript import display

sample_list =['Science', 'English','ICT', 'Math', 'Filipino'] # specifying list

display(sample_list,target='output')
display(f'{sample_list[2]}', target='output')

calc-btn = ('milktea', 'ice tea', 'royal', 'cidra')
drinks1, drinks2, drinks3, drinks4 = calc-btn # unpacking a tuple

display (f'Atasha\'s favorite drink is {drinks1}', target= 'output')
display (f'Kelsey\'s favorite drink is {drinks2}', target= 'output')
display (f'Manuel\'s favorite drink is {drinks3}', target= 'output')
display (f'Marcus\'s favorite drink is {drinks4}', target= 'output')