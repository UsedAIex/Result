from flask import Flask
from flask import url_for, request

app = Flask(__name__)


@app.route("/")
def name_of_operation():
    return "Миссия Колонизация Марса"


@app.route("/index")
def slogan_of_operation():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    text = ["Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!"]
    return "<br>".join(text)


@app.route("/image_mars")
def mars():
    return f"""
<html>
    <head>
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='image/mars2.jpg')}">
        <p>Вот она какая, красная планета.</p>
    </body>
</html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""
<html>
    <head>
        <title>Привет, Марс!</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/main2.css')}" >
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='image/mars2.jpg')}">
        <div class="alert alert-secondary" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-success" role="alert">    
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-secondary" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div  class="alert alert-warning" role="alert">
            И начнем с Марса!
        </div>
        <div  class="alert alert-danger" role="alert">
            Присоединяйся!
        </div>
    </body>
</html>"""


@app.route("/selection", methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="text">
                                    <input type="text" class="form-control" id="text" placeholder="Введите имя" name="text">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Высшее</option>
                                          <option>Не высшее</option>
                                          <option>Среднее</option>
                                          <option>Какое-то</option>
                                          <option>Ничего из выше перечисленного</option>
                                        </select>
                                     </div>
                                     <div>
                                        <label for="form-check">Какие у Вас профессии?</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_2" for="acceptRules">Пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_3" for="acceptRules">Строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_4" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_5" for="acceptRules">Врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_6" for="acceptRules">Инженер по терраформированию</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_7" for="acceptRules">Климатолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_8" for="acceptRules">Специалист по радиационной защите</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_9" for="acceptRules">Астрогеолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_10" for="acceptRules">Гляциолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_11" for="acceptRules">Инженер жизнеобеспечения</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_12" for="acceptRules">Метеоролог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_13" for="acceptRules">Оператор марсохода</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_14" for="acceptRules">Киберинженер</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_15" for="acceptRules">Штурман</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label_16" for="acceptRules">Пилот дронов</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        # print(request.form['email'])
        # print(request.form['password'])
        # print(request.form['class'])
        # print(request.form['file'])
        # print(request.form['about'])
        # print(request.form['accept'])
        # print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet>')
def greeting(planet):
    if planet == 'Меркурий':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet}!</h1>
                        <h2>Эта планета ближе к Солнцу</h2>
                      <div class="alert alert-primary" role="alert">
                        Самая ближайшая к Солнцу планета
                        </div>
                        </div>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                                <div class="alert alert-danger" role="alert">
                        Плутон
                        </div>
                              </body>
                      </body>
                    </html>'''
    elif planet == 'Венера':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Эта планета ближе к Меркурию</h2>
                                <div class="alert alert-success" role="alert">
                                Самая горячая планета Солнечной системы
                                </div>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                                <div class="alert alert-danger" role="alert">
                        Плутон
                        </div>
                              </body>
                            </html>'''
    elif planet == 'Земля':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Подсказка: Плутон</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Эта планета ближе к Венере</h2>
                                <div class="alert alert-info" role="alert">
                        Самая живучая планета
                        </div>
                              </body>
                            </html>'''
    elif planet == 'Марс':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Эта планета ближе к Земле</h2>
                                <div class="alert alert-primary" role="alert">
                                Вы наверное не замечали, но эта планета краснеет, когда вы смотрите на нее
                                </div>
                              </body>
                            </html>'''
    elif planet == 'Юпитер':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Эта планета ближе к Марсу</h2>
                                <div class="alert alert-secondary" role="alert">
                                Ученые скрывают от нас правду!!!
                                </div>
                                <div class="alert alert-danger" role="alert">
                                На самом деле, Юпитер не планета, а большой воздушный шарик с газами внутри
                                </div>
                              </body>
                            </html>'''
    elif planet == 'Сатурн':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Эта планета ближе к Юпитеру</h2>
                                <div class="alert alert-dark" role="alert">
                                Земледельная планета
                                </div>
                              </body>
                            </html>'''
    elif planet == 'Уран':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Эта планета ближе к Сатурну</h2>
                                <div class="alert alert-info" role="alert">
                                Огромный рудник, размером с планету
                                </div>
                              </body>
                            </html>'''
    elif planet == 'Нептун':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Эта планета ближе к Урану</h2>
                                <div class="alert alert-warning" role="alert">
                                Римский бог воды
                                </div>
                              </body>
                            </html>'''
    elif planet == 'Плутон':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {planet}!</h1>
                                <h2>Не планета СС</h2>
                                <div class="alert alert-success" role="alert">
                                До 2006 года была в Солнечной системе
                                </div>
                                <div class="alert alert-info " role="alert">
                                Но после ученые перестали считать Плутон планетой и убрали из Солнечной системы
                                </div>
                              </body>
                            </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                   <link rel="stylesheet"
                                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                   crossorigin="anonymous">
                                    <title>Результаты</title>
                                  </head>
                                  <body>
                                    <h1>Результаты отбора</h1>
                                    <h2>Претендента на участие в миссии {nickname}:</h2>
                                    <div class="alert alert-success" role="alert">
                                    Поздравляем! Ваш рейтинг после {level} этапа отбора
                                    </div>
                                    <h3>составляет {rating}!</h3>
                                    <div class="alert alert-warning" role="alert">
                                    Желаем удачи!
                                    </div>
                                  </body>
                                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
