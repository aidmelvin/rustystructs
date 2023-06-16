// // use pyo3::prelude::*;

// trait StackAttribute {
//     fn create(&self);
// }

// impl StackAttribute for i128 {
//     fn create(&self) { 
//         println!("i128 was passed");
//     }
// }

// impl StackAttribute for &str {
//     fn create(&self) { 
//         println!("String was passed");
//     }
// }


// // #[pyclass]
// pub struct StackInteger {
//     data: Vec<i128>,
// }

// // #[pymethods]
// impl StackInteger {
    
//     // #[staticmethod]
//     pub fn new() -> StackInteger {
//         StackInteger { data: Vec::new() }
//     }

//     pub fn new(value: i128) -> StackInteger {
//         StackInteger { data: vec![value] }
//     }

//     pub fn add(&mut self, value: i128) {
//         self.data.push(value);
//     }

//     pub fn pop(&mut self) -> Option<i128> {
//         if self.data.is_empty() {
//             return None;
//         }

//         let top = self.data.swap_remove(self.data.len() - 1);
//         Some(top)
//     }

//     pub fn peek(&mut self) -> Option<i128> {
//         if self.data.is_empty() {
//             return None;
//         }

//         Some(self.data[self.data.len() - 1])
//     }

// }

// // #[pyclass]
// pub struct StackString {
//     data: Vec<String>,
// }

// // #[pymethods]
// impl StackString {
    
//     // #[staticmethod]
//     pub fn new() -> StackString {
//         StackString { data: Vec::new() }
//     }

//     pub fn add(&mut self, value: String) {
//         self.data.push(value);
//     }

//     pub fn pop(&mut self) -> Option<String> {
//         if self.data.is_empty() {
//             return None;
//         }

//         let top = self.data.swap_remove(self.data.len() - 1);
//         Some(top)
//     }

//     pub fn peek(&mut self) -> Option<String> {
//         if self.data.is_empty() {
//             return None;
//         }

//         Some(self.data[self.data.len() - 1].clone())
//     }

// }

// #[macro_export]
// macro_rules! stack {
//     ($e:expr) => { StackAttribute::create(&$e) };
// }

// fn main() {
//     let my_stack = stack!(4);
// }

fn main() {

}
