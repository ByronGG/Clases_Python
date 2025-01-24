#include <iostream>
#include <string>
#include <fstream> // Liberia para trabajar con TXT (ficheros)
#include <vector> // Liberia para Vectores

/*
Crear un CRUD con un switch que sea de ficheros. 
Combinar clases de programación de switch, ficheros, vectores, if, for (iteraciones).
Solo se ocuparia la clase 1, 2, 3, 7, y tal vez 8. (repositorio GitHub)
*/

/*
En el switch debe tener las opciones (a, b, c, d, e, f)
    -a: Crear el archivo txt con nombre proporcionado por el usuario
    -b: Permitir al usuario agregar lineas de texto al archivo hasta que escriba "salir"
    -c: Leer todo el contenido del txt e imprimirlos en consola
    -d: Actualzar una línea específica (Muestra el contenido del fichero y permitir al usuario seleccionar y moficiar una linea)
    -e: Eliminar todo el contenido del fichero, SIN ELIMINAR el txt
    -f: Salir del programa
*/

using namespace std;
int main() {
    char editornotas;
    string textogeneral, input_a, input_b, input_c_selectlinea, input_c_informacion, input_d_selectlinea;
    char optionselect = '\0'; // inicializar la opción para el switch
    /*
    Un Do - While siempre al final de la llave del Do va el while con la condicón de cierre
    */
    do { 
        // En bloque "do" va el menú antes de entrar al bucle switch
        cout << "a. Create" << endl;
        cout << "b. Read" << endl;
        cout << "c. Update" << endl;
        cout << "d. Delete" << endl;
        cout << "Ingrese una opción: " << endl;
        cin >> optionselect; // Leemos la opción del usuario para el switch
        switch (optionselect){
        case 'a': 
            cout << "Escribe lo que quieres añadir al bloc de notas" << endl;
            cin >> input_a;
            textogeneral.append(input_a);
            break;
        case 'b': 
            cout << "Escribe el numero de linea que quieras leer del bloc de notas" << endl;
            cin >> input_b;
            cout << textogeneral.compare(input_b) << endl;
            break;
        case 'c':
            cout << "Escribe el numero de linea que quieras actualizar" << endl;
            cin >> input_c_selectlinea;
            cout << "Escribe la informacion que quieres sustituir por" << endl;
            cin >> input_c_informacion;
            break;
        case 'd':
            cout << "Selecciona la linea que quieras eliminar" << endl;
            cin >> input_d_selectlinea;
            break;
        }
    } while(optionselect == 'e');
}