#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{

	int i;
	PyListObject *obj = (PyListObject *)p;

	prrintf("[*] Size of the Python List = %d", PyList_Size(p));
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name;
}
