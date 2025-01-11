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

    Método	Descripción	Clases
    -------------------------------------------------------------------------------------------------------------------------
    .open("ruta", modo)	        Abre un archivo con una ruta y un modo específico.	                ifstream, ofstream, fstream
    .close()	                Cierra el archivo y libera recursos.	                            ifstream, ofstream, fstream
    .is_open()	                Retorna true si el archivo está abierto correctamente.	            ifstream, ofstream, fstream
    .write(char*, size)	        Escribe datos binarios en el archivo.	                            ofstream, fstream
    .read(char*, size)	        Lee datos binarios del archivo.	                                    ifstream, fstream
    .getline()	                Lee una línea completa de un archivo de texto.	                    ifstream, fstream
    <<	                        Operador para escribir datos en el archivo (texto).	                ofstream, fstream
    >>	                        Operador para leer datos del archivo (texto).	                    ifstream, fstream
    .eof()	                    Retorna true si se ha alcanzado el final del archivo.	            ifstream, fstream
    .good()	                    Verifica si el flujo está en buen estado.	                        ifstream, ofstream, fstream
    .fail()	                    Verifica si el flujo falló en una operación.	                    ifstream, ofstream, fstream
    .bad()	                    Verifica si hay un error grave (como pérdida de datos).	            ifstream, ofstream, fstream
    .seekg(pos)	                Mueve el puntero de lectura a una posición específica.	            ifstream, fstream
    .seekp(pos)	                Mueve el puntero de escritura a una posición específica.	        ofstream, fstream
    .tellg()	                Retorna la posición actual del puntero de lectura.	                ifstream, fstream
    .tellp()	                Retorna la posición actual del puntero de escritura.	            ofstream, fstream
    .flush()	                Fuerza la escritura del buffer al archivo.	                        ofstream, fstream

*/

#include <iostream>
#include <fstream> // Libreria para trabajar con ficheros
#include <map>
#include <iomanip>

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

    cout<<"------------------------------------CREAR & ESCRIBIR BINARIO---------------------------------------------------"<<endl;

    // Abrir archivo en modo binario
    ifstream archivoBinario_1("archivo_binario.bin", ios::in | ios::binary);

    //verifuca si se abrio correctamente
    if(archivoBinario_1.is_open()){
        int numero;
        double decimal;
        char texto[30]; // Array para alamacenar la cadena de texto

        // Leer los datos en el mismo orden que se escribieron
        archivoBinario_1.read(reinterpret_cast<char*>(&numero), sizeof(numero)); // 110010000000000010000 -> 1638416
        archivoBinario_1.read(reinterpret_cast<char*>(&decimal), sizeof(decimal));
        archivoBinario_1.read(texto, sizeof(texto));

        // Monstrar los datos leídos
        cout<<"Datos leidos del archivo binario: "<<endl;
        cout<<"Numero entero: "<<numero<<endl;
        cout<<"Numero decimal: "<<decimal<<endl;
        cout<<"Texto: "<<texto<<endl;

        // Cerrar el archivo
        archivoBinario_1.close();
    } else{
        cerr<<"No se pudo leer el archivo binario"<<endl;
    }

    cout<<"---------------------------------------LEER BINARIO---------------------------------------------------"<<endl;



cout<<"---------------------------------------EJERCICIO---------------------------------------------------"<<endl;

    ifstream archivo("vuelos.txt"); // Abrir el archivo de texto

    // Verificar si se avrio el archivo
    if(!archivo.is_open()){
        cerr<<"Error: No se pudo abrir el archivo."<<endl;
        return -1;
    }

    map<string, int> contador; // Mapa para contar las combinaciones
    string puntero_linea; // <- linea (el que lee linea por linea)

    // Leer lina por linea
    while(getline(archivo, puntero_linea)){
        if(puntero_linea.length() >= 2){ // Aseguira que la linea tenga al menos 2 caracteres
            string dosLetras = puntero_linea.substr(0, 2); // Obtener las primeras dos letras de la linea
            contador[dosLetras]++; // Incrementa el contador de una combinacion
        }
    }

    archivo.close(); // Cerramos el archivo

    // Calcular el promedio de ocurrencias
    int totalCombinaciones = contador.size();
    int totalOcurrencias = 0;

    for(const auto &par : contador){
        totalOcurrencias += par.second;
    }

    double promedio = totalCombinaciones > 0 ? static_cast<double>(totalOcurrencias) / totalCombinaciones : 0.0;

    // Mostrar resultados
    cout << "Combinaciones de la primera dos letras y sus ocurrencias: "<<endl;
    cout<<"--------------------------------------------------------------"<<endl;
    for(const auto &par: contador){
        cout<<par.first<<": "<<par.second<<" veces."<<endl;
    }

    cout<<"--------------------------------------------------------------"<<endl;
    cout<<"Promedio de ocurrencias por combinación de vuelo: "<<fixed<<setprecision(2)<<promedio<<endl;

    return 0;
}