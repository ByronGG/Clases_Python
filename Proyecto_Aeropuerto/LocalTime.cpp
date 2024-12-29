#include <iostream>
using namespace std;

class LocalTime{
    private:
    int minutes;

    public:
    // Constructor
    LocalTime() : minutes(0){}

    void set_time(int hours, int minutes){
        this->minutes = hours * 60 + minutes;
    }
    // Obtener la hora
    int get_hour() const{
        return minutes / 60;
    }
    // Obtener los minutos
    int get_minute() const{
        return minutes % 60;
    }

    bool is_valid() const{
        return minutes >= 0 && minutes < 24 * 60;
    }

    //Mostrar tiempo
    void print() const{
        if(is_valid()){
            cout<<get_hour()<<":"<<get_minute()<<endl;
        }else{
            cout<<"Invalid time"<<endl;
        }
    }
};