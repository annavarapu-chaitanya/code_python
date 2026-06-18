College = 'Codegnan'

def Student(name, marks):
    original_fee = 50000

    if marks > 90:
        print('Grade A')
        discount = (20 / 100) * original_fee
        fee = original_fee - discount
        print(f'Your fee: {fee}')

    elif marks > 80:
        print('Grade B')
        discount = (15 / 100) * original_fee
        fee = original_fee - discount
        print(f'Your fee: {fee}')

    elif marks > 70:
        print('Grade C')
        discount = (10 / 100) * original_fee
        fee = original_fee - discount
        print(f'Your fee: {fee}')

    else:
        print(f'Your fee: {original_fee}')

name = input('Enter Name: ')
marks = int(input('Enter Marks: '))

Student(name, marks)
