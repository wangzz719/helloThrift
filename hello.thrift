service Hello{
    string hello_string(1:string para),
    i32 hello_int(1:i32 para),
    bool hello_boolean(1:bool para),
    void hello_void(),
    string hello_null()
}