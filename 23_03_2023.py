
str1="Happy";
###############################3
print(str1[2]);
print(str1[-1]);
print(str1[-5]);
##slicing
print(str1[1:2]);
print(str1[:]);

##convert number to string;
number=10.7464;
numberToFloat=float(number);
print(numberToFloat);
print(type(numberToFloat))
num='67.90';
print(float(num))
print(type(num))

#slicing###################
sl1='country';
print(sl1[1:3]);
print(str1[:])
print(sl1[:])
print(sl1[0:3]);
print(sl1[2:3]);
################################
sl2='Bangladesh';
print(sl2[1:3]);
print(sl2[1:4]);
print('[0:2:4] :',sl2[0:2:4]);
print('[3:5]',sl2[3:5]);

##strings are immutable#################
a='Happy';
b='Be'+' '+''+a;
print(b);

##String replication #################
rep='rifat'*3
print(rep)
print('shahriar'*4);

##Formatting string#################
ss1='My name is %s'%'Rifat';
print(ss1);
name='Rifat'
ss2=f' My name is {name}';
print(ss2);

s_1='My name is %s ,I am %d years old' %("Rifat",7);
print(s_1);

myName='My  First Name is %s and my Last Name is %s' %("Abu Al Shahriar","Rifat");
print(myName);

formatting_floting='The Cartoon contains %f kilos potatos' %(90.78);
print(formatting_floting);
isMarried=True;

#######3
boolean_formatting= 'You are  married {} or False '.format(isMarried);
print(boolean_formatting)
n='Rifat';
age=26
s_11='My name is {} I am {} years old'.format(n,age);
print(s_11);

######################
name='Abu Al Shahriar Rifat';
print(name.upper());
firstName='Shahriar';
print(firstName.lower());
print(firstName.startswith('S'));
print(firstName.endswith('r'));
print(name.count('h'));
print(name.islower())
print(name.isupper());
print(name.find('h'));
print(name.replace("R","S"));
print(name.index('S'));
print(name.index('R'));
print(name.split(' '));
print(len(name));


##Iterating throung loope
a='Shahriar';
count=0;
for letter in a:
    if(letter=='S'):
        count+=1
print(count ,'has found in the string')


## String membership test
a='Happy';
print('p' in a);
print('k' not in a);





