/*  Ficheros
    -------------------------------------------------------------------------------------------------------------------------
    Los ficheros se utilizan para almacenar y manipular datos de forma persistente fuera del tiempo de ejecución del programa. 
    - Texto: Contienen datos legibles como caracteres y númericos (.txt, .csv)
    - Binarios: Alamenan datos en formato binario, ocupan menos espacio y son más rápidos de procesar (.dat, .bin)

    Librerias necesarias para trabajar ficheros
    <fstream> para manejar ficheros, incluye tres clases principales:
    std::ifstream: Para leer archivos (entrada)
    std::ofstream: Para escribir un archivos (salida)
    std::fstream: Para leer y escribir un archivo

    -Para un archivo se utiliza el método .open()
        ifstream inputFile;
        inputFile.open("archivo.txt"); // Leer
        ofstream outputFile("archivo.txt") // Escribir
    - Siempre tienes que cerrar un archivo despúes de usarlo .close()
        inputFile.close()
        outputFile.close()
    - Escribir un archivo, se utiliza el operador de entrada '<<'
        ofstream archivo("archivo.txt");
        if(archivo.is_open()){
            archivo << "Hola arturo"<<endl;
            archivo.close();
        }
    Usa el is_open() para evitar errores en bus de entrada
    -NOTA: Buena práctica para menejo de fichero en C++: 
        Antes de operar con fichero, verifica que se haya abierto correctametne usando .is_open() o comprobando el estado del flujo
        if(!archivo.is_open()){
            cerr <<"Error al abrir el archivo "<<endl;
            return  -1;
        }
    - Leer un arachivo, se utuliza el operador de salida '>>' o funciones como getline
        ifstream archivo("archivo.txt");
        string linea;
        if (archivo.is_open()){
            while(getline(archivo, linea)){
                cout<<linea<<endl;
            }
            archivo.close();
        }
    MODOS DE APERTURA
    ios::in - Modo lectura
    ios::out - Modo escritura
    ios::app - Añadir datos al FINAL DEL ARCHIVO
    ios::binary - Modo binario
    ios::trunc - Borrar el contenido AL ABRIR

    MENEJO DE ERRORES
    Verifica si el archivo es´ta abierto correctamento
    ifstream archivo("archivo.txt");
    if(archivo){
        //código...
    }

    ARCHIVO BINARIO
    .write()
    .read()
    Leer archivo binario
    ifstream archivo("datos.bin", ios::in | ios::binary);
    int numero;
    archivo.read(reinterpret_cast<char*>(&numero), sizeof(numero));
    cout<<"niumero leido: "<<numero<<endl;
    archivo.close()
*/

#include <iostream>
#include <fstream> // Libreria para trabajar con ficheros

using namespace std;

int main(){

    // //Escribir en un archivo
    ofstream archivoEscritura("ejemplo.txt"); //ofstream le da permiso de ESCRIBIR a nuestro fichero (.txt)
    if(archivoEscritura.is_open()){
        archivoEscritura <<"Hola Arturo"<<endl;
        archivoEscritura <<"Como estas?"<<endl;
        archivoEscritura <<"Adios"<<endl;
        archivoEscritura.close();
    } else {
        cerr<<"No se pudo abrir el archivo para escribir"<<endl;
    }
    cout<<"----------------------------------------ESCRIBIR TXT-------------------------------------------------------"<<endl;

    // Leer del archivo
    ifstream archivoLectura("ejemplo.txt"); // ifstream le da permiso de LEER a nuestro ficher (.txt)
    string linea; // nuestro puntero para ir leyendo linea por linea
    if(archivoLectura.is_open()){
        while(getline(archivoLectura, linea)){
            cout<<linea<<endl; // Impresion por consola
        }
        archivoLectura.close();
    } else {
        cerr<<"No se pudo abrir el archivo para leer"<<endl;
    }
    cout<<"------------------------------------------LEER TXT-----------------------------------------------------"<<endl;

    //Crear y arbir un archivo binario
    ofstream archivoBinario("archivo_binario.bin", ios::out | ios::binary); //Modo apertura combinado out binary

    //Verificar si se abrió correctamente
    if(archivoBinario.is_open()){
        //Datos a escribir en el arhivo
        int numero = 1638416;
        double decimal = 12818.3201;
        char texto[] = "Hola, Arturo en binario";

        //Escribir los datos en el archivo
        archivoBinario.write(reinterpret_cast<char*>(&numero), sizeof(numero)); //1638416 -> binario 110010000000000010000
        archivoBinario.write(reinterpret_cast<char*>(&decimal), sizeof(decimal)); //12818.3201 -> binario 11001000010010.01010001111100100001001011010111011101
        archivoBinario.write(texto, sizeof(texto)); // Hola, Arturo en binario -> binario 01001000 01101111 01101100 01100001 00101100 00100000 01000001 01110010 01110100 01110101 01110010 01101111 00100000 01100101 01101110 00100000 01100010 01101001 01101110 01100001 01110010 01101001 01101111 

        //Cerrar el archivo
        archivoBinario.close();
        cout<<"Archivo binario creado y datos escritos correctamente."<<endl;
    } else {
        cerr<<"No se pudo crear el archivo binario"<<endl;
    }

    

    return 0;
}