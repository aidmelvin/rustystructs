use pyo3::{prelude::*, types::PyType};
mod models;
use pyo3::exceptions::PyTypeError;
use models::stack::integer_stack::IntegerStack;
use models::stack::string_stack::StringStack;
use models::heap::integer_heap::IntegerHeap;
use models::heap::string_heap::StringHeap;
use models::dequeue::integer_dequeue::IntegerDequeue;
use models::dequeue::string_dequeue::StringDequeue;

/// Heap(is_min: bool, /)
/// --
///
/// This function creates a new Heap. If is_min is True, it will be a min heap. Otherwise, it is a max heap.
#[pyfunction]
fn Heap(value: &PyType, is_min: bool) -> Result<PyObject, PyErr> {
    let gil = Python::acquire_gil();
    let py = gil.python();
    let arg_type = value.to_string();

    if arg_type.eq_ignore_ascii_case("<class 'int'>") {
        return Ok(IntegerHeap::new(is_min).into_py(py))
    } else if arg_type.eq_ignore_ascii_case("<class 'str'>") {
        return Ok(StringHeap::new(is_min).into_py(py))
    } else {
        return Err(PyTypeError::new_err("Type argument supplied must be either 'int' or 'str'"))
    }
}

/// Dequeue()
/// --
///
/// This function creates a new double-ended queue
#[pyfunction]
fn Dequeue(value: &PyType) -> Result<PyObject, PyErr> {
    let gil = Python::acquire_gil();
    let py = gil.python();
    let arg_type = value.to_string();

    if arg_type.eq_ignore_ascii_case("<class 'int'>") {
        return Ok(IntegerDequeue::new_empty().into_py(py))
    } else if arg_type.eq_ignore_ascii_case("<class 'str'>") {
        return Ok(StringDequeue::new_empty().into_py(py))
    } else {
        return Err(PyTypeError::new_err("Type argument supplied must be either 'int' or 'str'"))
    }
}

/// Stack()
/// --
///
/// This function creates a new stack
#[pyfunction]
fn Stack(value: &PyType) -> Result<PyObject, PyErr> {
    let gil = Python::acquire_gil();
    let py = gil.python();
    let arg_type = value.to_string();

    if arg_type.eq_ignore_ascii_case("<class 'int'>") {
        return Ok(IntegerStack::new().into_py(py))
    } else if arg_type.eq_ignore_ascii_case("<class 'str'>") {
        return Ok(StringStack::new().into_py(py))
    } else {
        return Err(PyTypeError::new_err("Type argument supplied must be either 'int' or 'str'"))
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn rustystructs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(Heap, m)?)?;
    m.add_function(wrap_pyfunction!(Dequeue, m)?)?;
    m.add_function(wrap_pyfunction!(Stack, m)?)?;
    Ok(())
}
