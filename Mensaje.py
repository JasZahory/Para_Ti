print("Iniciando protocolo de declaración...")
print("Cargando sentimientos...")
print("")

corazon = {
    "En Python": "me encantas y no hay excepción que atrape esto",
    "En SQL": "SELECT * FROM mis_pensamientos WHERE tú = 'tú' AND yo = 'yo';",
    "En JavaScript": "miCorazon.latidos.forEach(() => console.log('pienso en ti'));",
    "En HTML": "<h1 style='color:pink'>Eres mi bug favorito</h1>",
    "En Git": "git merge tú conmigo --no-ff -m 'Haciéndolo oficial'",
    "En Bash": "while true; do echo 'te extraño'; sleep 1; done",
    "En mi lenguaje": "No necesito código para saber que me haces sonreír"
}

for lenguaje, frase in corazon.items():
    print(f"💻 {lenguaje}: {frase}")
    print("")

print("╔════════════╗")
print("║  Resultado: Compilación exitosa   ║")
print("║  Estado: Me encantas tú           ║")
print("╚════════════╝")
print("\nPD: Si esto te sacó una sonrisa, ya valió la pena escribirlo")
