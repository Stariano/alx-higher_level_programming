#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{

	PyListObject *obj = (PyListObject *)p;

	prrintf("[*] Size of the Python List = %d", PyList_Size(obj))
};
