import flet as ft
import openai
import pywhatkit

openai.api_key = "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"


def main(page: ft.Page):
    def gpt(e):
        if not altura1.value:
            altura1.error_text = "Para que possamos fazer sua dieta é nescessario que saibamos sua altura."
            page.update()
        if not peso1.value:
            peso1.error_text = "Para que possamos fazer sua dieta é nescessario que saibamos seu peso."
            page.update()
        if not idade.value:
            idade.error_text = "Para que possamos fazer sua dieta é nescessario que saibamos sua idade."
            page.update()
        page.clean()
        page.update()
        tamanho = float(altura1.value) ** 2
        massa = float(peso1.value)
        imc = massa / tamanho
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"""faça de conta que você é o melhor nutricionista do mundo, e crie 
uma dieta para uma pessoa com o imc de {imc}, com {idade} anos de idade, com {prb.value}, do sexo {sex} e com o objetivo
de {obj}."""}])
        real_response = response["choices"][0]["message"]["content"]
        v_response = ft.Text(value=real_response)
        imc_response = ft.Text(value=f'')
        if imc < 16:
            imc_response.value = f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 1."

        elif 16 <= imc < 17:
            imc_response.value = f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 2."

        elif 17 <= imc < 18.5:
            imc_response.value = f"seu imc é de {imc}, isso indica que você tem o baixo peso de grau 3."

        elif 18.5 <= imc < 25:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está na faixa de peso ideal."

        elif 25 <= imc < 30:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com sobrepeso."

        elif 30 <= imc < 35:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com obesidade de grau 1."

        elif 35 <= imc < 40:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com obesidade de grau 2."

        elif imc > 40:
            imc_response.value = f"seu imc é de {imc}, isso indica que você está com obesidade de grau 3."

        veridc_response = str(v_response)
        r = veridc_response.split()
        resposta = " ".join(r[2:])
        royal_response = resposta.replace("\\n", '\n')
        r_response = royal_response.replace("{" and "}", "")
        rr_response = r_response.replace("'", "")
        pywhatkit.sendwhatmsg_instantly(str(num.value), rr_response)
        page.add(imc_response, v_response)

    page.scroll = "always"
    page.title = "Healthy Sesi"
    t = ft.Text(value="Qual sua altura em metros?")
    altura1 = ft.TextField(label="Digite sua altura aqui!")
    t2 = ft.Text(value="Qual seu peso?")
    peso1 = ft.TextField(label="Digite seu peso aqui!")
    t3 = ft.Text(value="Qual sua idade?")
    idade = ft.TextField(label="Digite sua idade aqui!")
    t4 = ft.Text(value="Qual seu sexo?")
    sex = ft.TextField(label="Digite seu sexo aqui!")
    t5 = ft.Text(value="Qual seu objetivo com a dieta?")
    obj = ft.TextField(label="Digite seu objetivo aqui!")
    t6 = ft.Text(value="Você possui algum problema da saúde?")
    prb = ft.TextField(label="Digite seu(s) problemas de saúde aqui!")
    t7 = ft.Text(value="Qual seu número de celular?")
    num = ft.TextField(label="Digíte seu número de celular (com ddd) aqui!")
    btns = ft.ElevatedButton("clique aqui", on_click=gpt)
    page.add(ft.Column([t, altura1]), ft.Column([t2, peso1]), ft.Column([t3, idade]), ft.Column([t4, sex]),
             ft.Column([t5, obj]), ft.Column([t6, prb]), ft.Column([t7, num]), btns)


ft.app(target=main)
# t3, idade, t4, sex

