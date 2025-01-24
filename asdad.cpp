#include <iostream>
using namespace std;
#include <string>
/*
Crear un CRUD con un switch que sea de ficheros. 
Combinar clases de programación de switch, ficheros, vectores, if, for (iteraciones).
Solo se ocuparia la clase 1, 2, 3, 7, y tal vez 8. (repositorio GitHub)
*/
int main() {
    char editornotas;
    //char optionselect;
    do {
        switch (optionselect){
            string textogeneral;
            cout << "a. Create" << endl;
            cout << "b. Read" << endl;
            cout << "c. Update" << endl;
            cout << "d. Delete" << endl;
            cout << "imprime" << endl;
            cin >> optionselect;
        case 'a': 
            string input_a;
            cout << "Escribe lo que quieres añadir al bloc de notas" << endl;
            cin >> input_a;
            textogeneral.append(input_a);
            break;
        case 'b':
            string input_b;
            cout << "Escribe el numero de linea que quieras leer del bloc de notas" << endl;
            cin >> input_b;
            cout << textogeneral.compare(input_b) << endl;
            break;
        case 'c':
            string input_c_selectlinea;
            string input_c_informacion;
            cout << "Escribe el numero de linea que quieras actualizar" << endl;
            cin >> input_c_selectlinea;
            cout << "Escribe la informacion que quieres sustituir por" << endl;
            cin >> input_c_informacion;
            break;
        case 'd':
            string input_d_selectlinea;
            cout << "Selecciona la linea que quieras eliminar" << endl;
            cin >> input_d_selectlinea;
            break;
        }
    }
}