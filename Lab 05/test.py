import segno

from pallindrome import isPallindrome

link = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.static-collegedunia.com%2Fpublic%2Fcollege_data%2Fimages%2Fcampusimage%2F1522146873Apple%2520Lab.jpg&f=1&nofb=1&ipt=7e32d9f6e4294c7a2cb35833cf764c653398363387acf8b3927b84a8964ce462&ipo=images"

def test_pallindrome():
    check = [0, 1, 11, 12, 131, 155]
    answer = [True, True, True, False, True, False] 
    for i in range(len(check)):
        if isPallindrome(check[i]) != answer[i]:
            print("The code is wrong, Try Again")
            break
    else:
        qr_code = segno.make(link)
        qr_code.save("next_location.png")
        print("Scan the QR code Named, Next Clue")

if __name__ == "__main__":
    test_pallindrome()
