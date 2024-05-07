from jinja2 import Environment, FileSystemLoader
import time


def main():
    
    first_name = input("Имя (+отчество): ")
    last_name = input("Фамилия: ")
    added_number = input("Добавочный номер: ")
    mobile_number = input("Мобильный телефон: ")
    position = input("Должность: ")
    email = input("Почта: ")
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('new_template_r3.html.jinja2')
    # print(output_from_parsed_template)
    with open(f"./output/{email}_signature.html", mode="w", encoding='utf-8') as fh:
        fh.write(template.render({"first_name":first_name,
                                  "last_name": last_name,
                                  "added_number":added_number,
                                  "mobile_number":mobile_number,
                                  "position": position,
                                  "email":email}))

    print("Успешно")
    time.sleep(3)

if __name__ == "__main__":
    main()