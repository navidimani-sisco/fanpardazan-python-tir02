import math
# 1. دریافت طول و عرض سالن مستطیلی
length = int( input("طول") )
width = int( input("عرض") )
# 2. محاسبه مساحت سالن ها 
surface = length * width

# 3. محاسبه محیط مستطیل
rectangle_perimeter = 2 * length + 2 * width
# 4. محاسبه محیط مربع
square_length = math.sqrt(surface)
square_perimeter = 4 * square_length
# 5. یافتن بهترین محیط
if square_perimeter < rectangle_perimeter:
  print("مربع بهتر است")
else:
  print("مستطیل بهتر است")
