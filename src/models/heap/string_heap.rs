use pyo3::prelude::*;


#[pyclass]
pub struct StringHeap {
    is_min_heap: bool,
    data: Vec<String>,
}

#[pymethods]
impl StringHeap {
    
    #[staticmethod]
    pub fn new(is_min: bool) -> Self {
        StringHeap { is_min_heap: is_min, data: Vec::new() }
    }

    pub fn add(&mut self, value: String) {
        self.data.push(value);
        let index = self.data.len() - 1;
        self.sift_up(index);
    }

    pub fn remove_top(&mut self) -> Option<String> {
        if self.data.is_empty() {
            return None;
        }

        let top = self.data.swap_remove(0);
        self.sift_down(0);
        Some(top)
    }

    pub fn is_empty(&mut self) -> Option<bool> {
        return Some(self.data.len() == 0)
    }

    pub fn size(&mut self) -> Option<usize> {
        return Some(self.data.len())
    }

    fn sift_up(&mut self, mut index: usize) {
        while index > 0 {
            let parent_index = (index - 1) / 2;

            if self.is_min_heap && self.data[parent_index] <= self.data[index] {
                break;
            }
            
            if !self.is_min_heap && self.data[parent_index] >= self.data[index] {
                break;
            }
            self.data.swap(parent_index, index);
            index = parent_index;
        }
    }

    fn sift_down(&mut self, mut index: usize) {
        let size = self.data.len();
        while index < size {
            let left_child_index = 2 * index + 1;
            let right_child_index = 2 * index + 2;

            let mut smallest = index;
            if self.is_min_heap {
                if left_child_index < size && self.data[left_child_index] < self.data[smallest] {
                    smallest = left_child_index;
                }
                if right_child_index < size && self.data[right_child_index] < self.data[smallest] {
                    smallest = right_child_index;
                }
            } else {
                if left_child_index < size && self.data[left_child_index] > self.data[smallest] {
                    smallest = left_child_index;
                }
                if right_child_index < size && self.data[right_child_index] > self.data[smallest] {
                    smallest = right_child_index;
                } 
            }

            if smallest == index {
                break;
            }
            self.data.swap(smallest, index);
            index = smallest;
        }
    }

}
