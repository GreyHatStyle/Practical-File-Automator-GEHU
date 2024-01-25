from Language_Selection import C_Complier
# Testing C_Compiler Class

ip3 = """3
Manas is good boy
he is okay with life
as always
2
This is good way
to check
1
I am done"""
obj = C_Complier("sp-string.c", 3, ip3)

ans = obj.get_output()
print(ans)


# Test Successfull!