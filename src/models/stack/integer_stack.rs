use pyo3::{prelude::*, types::PyType};
use pyo3::exceptions::PyTypeError;


#[pyclass]
pub struct IntegerStack {
    data: Vec<i128>,
}

#[pymethods]
impl IntegerStack {
    
    #[staticmethod]
    pub fn new() -> Self {
        IntegerStack { data: Vec::new() }
    }

    pub fn add(&mut self, value: i128) {
        self.data.push(value);
    }

    pub fn pop(&mut self) -> Option<i128> {
        if self.data.is_empty() {
            return None;
        }

        let top = self.data.swap_remove(self.data.len() - 1);
        Some(top)
    }

    pub fn peek(&mut self) -> Option<i128> {
        if self.data.is_empty() {
            return None;
        }

        Some(self.data[self.data.len() - 1])
    }

}
