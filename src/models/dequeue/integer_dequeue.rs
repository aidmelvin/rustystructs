
use std::sync::{Arc, Mutex};
use pyo3::prelude::*;

type NodeRef = Arc<Mutex<Node>>;
pub type NodeOption = Option<NodeRef>;

#[derive(Debug)]
pub struct Node {
    pub data: i128,
    pub next: NodeOption
}

impl Node {
    pub fn new(number: i128) -> NodeRef {
        Arc::new(Mutex::new(Node {
            data: number,
            next: None
        }))
    }
}

impl Drop for Node {
    fn drop(&mut self) {
        // println!("Node with this data -> '{}' just dropped", self.data);
    }
}

// Node iterator
#[pyclass]
pub struct ListNodeIterator {
    current: NodeOption
}

impl ListNodeIterator {
    pub fn new(start_at: NodeOption) -> Self {
        ListNodeIterator {
            current: start_at
        }
    }
}


impl Iterator for ListNodeIterator {
    type Item = NodeRef;

    fn next(&mut self) -> NodeOption {
        let current = &self.current;
        let mut result = None;

        self.current = match current {
            Some(ref current) => {
                result = Some(Arc::clone(current));
                match &current.lock().unwrap().next {
                    Some(next_node) => {
                        Some(Arc::clone(next_node))
                    },
                    _ => None
                }
            },
            _ => None
        };

        result
    }
}

#[derive(Debug)]
#[pyclass]
pub struct IntegerDequeue {
    head: NodeOption,
    tail: NodeOption,
    pub length: usize
}

#[pymethods]
impl IntegerDequeue {

    #[staticmethod]
    pub fn new_empty() -> Self {
        IntegerDequeue {
            head: None,
            tail: None,
            length: 0
        }
    }

    pub fn append_start(&mut self, text: i128) {
        let new_head = Node::new(text);

        match self.head.take() {
            Some(old_head) => {
                new_head.lock().unwrap().next = Some(Arc::clone(&old_head));

                match &self.tail {
                    None => {
                        self.tail = Some(Arc::clone(&old_head));
                    },
                    _ => ()
                }
            },
            _ => ()
        }

        self.head = Some(new_head);
        self.length = self.length + 1;
    }

    pub fn append_end(&mut self, text: i128) {

        match &self.head {
            Some(head) => {
                let new_tail = Node::new(text);

                match self.tail.take() {
                    Some(old_tail) => {
                        old_tail.lock().unwrap().next = Some(Arc::clone(&new_tail));
                    },
                    _ => {
                        head.lock().unwrap().next = Some(Arc::clone(&new_tail));
                    }    
                }

                self.tail = Some(new_tail);
                self.length = self.length + 1;

            },
            _ => {
                self.append_start(text);
            }
        }
    }

    pub fn pop_head(&mut self) -> Option<i128> {
        self.head.take().map(|old_head| {
            match old_head.lock().unwrap().next.take() {
                Some(new_head) => {
                    self.head = Some(Arc::clone(&new_head));
                },
                _ => {}
            }
            self.length = self.length - 1;
            old_head.lock().unwrap().data
        })
    }

    pub fn pop_end(&mut self) -> Option<i128> {
        self.tail.take().map(|old_tail| {

            let mut iterator = self.iter_node();
            let mut temp = iterator.next();
            

            for _ in 0..self.length - 2 {
                temp = iterator.next();
            }

            match temp {
                Some(node) => {
                    node.lock().unwrap().next = None;

                    if self.length > 2 {
                        self.tail = Some(Arc::clone(&node));
                    }
                },
                _ => {}
            }
            
            self.length = self.length - 1;
            old_tail.lock().unwrap().data 
        })
    }

    fn iter_node(&self) -> ListNodeIterator {
        match &self.head {
            Some(head) => {
                ListNodeIterator::new(Some(Arc::clone(head)))
            },
            _ => ListNodeIterator::new(None)
        }
    }

}