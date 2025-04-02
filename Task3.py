def decode(input_file, shift1, stop_word1, shift2, stop_word2, shift3, stop_word3, shift4, stop_word4):
    with open(input_file, "r", encoding="utf-8") as file:
        ciphertext = file.read()
    
    decrypted_text = ""
    shift = shift1  
    stage = 1  
    
   
    lines = ciphertext.splitlines()
    
    for line in lines:
        if "BEGINNING OF MESSAGE" in line or "END OF MESSAGE" in line:
            decrypted_text += line + "\n"
            continue
        
        decrypted_line = ""
        for char in line:
            if char.isalpha():
                shift_amount = shift % 26
                new_char = chr(((ord(char.lower()) - ord('a') - shift_amount) % 26) + ord('a'))
                if char.isupper():
                    new_char = new_char.upper()
                decrypted_line += new_char
            else:
                decrypted_line += char
        
        decrypted_text += decrypted_line + "\n"

       
        if stage == 1 and stop_word1 in decrypted_text:
            stage = 2
            shift = shift2  
        elif stage == 2 and stop_word2 in decrypted_text:
            stage = 3
            shift = shift3  
        elif stage == 3 and stop_word3 in decrypted_text:
            stage = 4
            shift = shift4  
        elif stage == 4 and stop_word4 in decrypted_text:
            break  

    return decrypted_text

input_file = "2025CGW Task 3 Input.txt"
shift1 = 4 #decode key until word "lie"
stop_word1 = "lie."  
shift2 = 7 #decode key until word "philosophee"
stop_word2 = "philosophee."  
shift3 = 16 #decode key until word "year"
stop_word3 = "year."  
shift4 = 2 #decode key until the last word in txt file
stop_word4 = "-----    END OF MESSAGE    -----"  

decrypted_text = decode(input_file, shift1, stop_word1, shift2, stop_word2, shift3, stop_word3, shift4, stop_word4)
print(decrypted_text)
