height = input('請輸入身高(m): ')
weight = input('請輸入體重(kg): ')
weight = float(weight)
height = float(height)
BMI = weight / height / height
BMI = float(BMI)
if BMI < 18.5:
    print('您的BMI為', BMI, '過輕')
elif BMI >= 18.5 and BMI <24:
    print('您的BMI為', BMI, '適中')
elif BMI >=24 and BMI <27:
    print('您的BMI為', BMI, '過重')
elif BMI >= 27 and BMI <30:
    print('您的BMI為', BMI, '輕度肥胖')
elif BMI >=30 and BMI <35:
    print('您的BMI為', BMI, '中度肥胖')
else:
    print('您的BMI為', BMI, '重度肥胖')
