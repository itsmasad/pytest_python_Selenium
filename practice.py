# Checking if the number is divisible by 10
# for i in range(1, 100):
#     if i % 10 == 0:
#         print(i)


# Checking Anagram Function
# def is_anagram(str1, str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()

#     return sorted(str1) == sorted(str2)

# word1 = "silent"
# word2 = "listen"

# if is_anagram(word1,word2):
#     print("It is an anagram")
# else:
#     print("not an anagram")



import pytest

@pytest.fixture(scope="function")
def setUp():
    print("This is setup")


def test_data():
    data = [
        ("Asad@gmail.com","Asad_Password"),
        ("Naveed@gmail.com","Naveed_Password"),
        ("Uzair@gmail.com","Uzair_password")
    ]
    return data

@pytest.mark.parametrize("username,password",test_data())
def test_Login(username,password):
    print(username,password)