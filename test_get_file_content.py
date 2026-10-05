from functions.get_file_content import get_file_content


result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")




result2 = get_file_content("calculator", "main.py")
print(result2)

#print(f"main.py length: {len(result2)}")
#print(f"main.py truncated: {'truncated' in result2}")


result3 = get_file_content("calculator", "pkg/calculator.py")
print(result3)
#print(f"calculator.py length: {len(result3)}")
#print(f"calculator.py truncated: {'truncated' in result3}")


result4 = get_file_content("calculator", "/bin/cat")
print(result4)
#print(f"/bin/cat length: {len(result4)}")
#print(f"/bin/cat truncated: {'truncated' in result4}")


result5 = get_file_content("calculator", "pkg/does_not_exist.py")
print(result5)
#print(f"does_not_exist.py length: {len(result5)}")
#print(f"does_not_exist.py truncated: {'truncated' in result5}")




