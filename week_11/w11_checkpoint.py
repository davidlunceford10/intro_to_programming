with open('week11/books.txt') as book_of_mormon_list:
    
    for line in book_of_mormon_list:
        bomlistStrip = line.strip()
        print(bomlistStrip)