use pyo3::{prelude::*, types::PyType};
use pyo3::exceptions::PyTypeError;

#[pyclass]
pub struct StringStack {
    data: Vec<String>,
}

#[pymethods]
impl StringStack {
    
    #[staticmethod]
    pub fn new() -> Self {
        StringStack { data: Vec::new() }
    }

    pub fn add(&mut self, value: String) {
        self.data.push(value);
    }

    pub fn pop(&mut self) -> Option<String> {
        if self.data.is_empty() {
            return None;
        }

        let top = self.data.swap_remove(self.data.len() - 1);
        Some(top)
    }

    pub fn peek(&mut self) -> Option<String> {
        if self.data.is_empty() {
            return None;
        }

        Some(self.data[self.data.len() - 1].clone())
    }

}
