#include <Python.h>
#include <iostream>

using namespace std;
int main() {
    Py_Initialize();
    // include python file directory into this code
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('../scripts')");

    //导入模块
    PyObject* pModule = PyImport_ImportModule("Endeffector_serial_monitor");

    if (!pModule)
    {
        cout << "Python get module failed: path to the py file not correct" << endl;
        return 0;
    }


    PyObject * pFunc = NULL;
    pFunc = PyObject_GetAttrString(pModule, "detecting_Serial");
    PyEval_CallObject(pFunc, NULL);


    Py_Finalize();
}
