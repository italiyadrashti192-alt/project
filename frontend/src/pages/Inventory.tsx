// import { useEffect, useState } from "react";
// import "./Inventory.css";

// interface InventoryItem {
//   _id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   minimum_stock: number;
//   supplier_id?: string;
// }

// interface InventoryResponse {
//   status: string;
//   count: number;
//   inventory: InventoryItem[];
// }

// function Inventory() {
//   const [inventory, setInventory] = useState<InventoryItem[]>([]);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState("");

//   useEffect(() => {
//     fetch("http://127.0.0.1:8000/inventory/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch inventory");
//         }

//         return response.json();
//       })
//       .then((data: InventoryResponse) => {
//         setInventory(data.inventory);
//         setLoading(false);
//       })
//       .catch((error) => {
//         console.error("Inventory API Error:", error);
//         setError("Unable to load inventory");
//         setLoading(false);
//       });
//   }, []);

//   return (
//     <main className="inventory-page">

//       {/* Page Header */}
//       <div className="inventory-header">
//         <div>
//           <p className="inventory-welcome">Inventory Management</p>
//           <h1>Inventory</h1>
//           <span>
//             Manage your restaurant ingredients and stock levels
//           </span>
//         </div>

//         <button className="add-inventory-btn">
//           + Add Inventory
//         </button>
//       </div>

//       {/* Loading */}
//       {loading && (
//         <div className="inventory-message">
//           Loading inventory...
//         </div>
//       )}

//       {/* Error */}
//       {error && (
//         <div className="inventory-error">
//           {error}
//         </div>
//       )}

//       {/* Inventory Table */}
//       {!loading && !error && (
//         <div className="inventory-table-container">

//           <table className="inventory-table">

//             <thead>
//               <tr>
//                 <th>Ingredient</th>
//                 <th>Quantity</th>
//                 <th>Unit</th>
//                 <th>Minimum Stock</th>
//                 <th>Status</th>
//               </tr>
//             </thead>

//             <tbody>
//               {inventory.map((item) => {

//                 const isLowStock =
//                   item.quantity <= item.minimum_stock;

//                 return (
//                   <tr key={item._id}>

//                     <td>
//                       <div className="ingredient-name">
//                         🥕 {item.ingredient_name}
//                       </div>
//                     </td>

//                     <td>
//                       <strong>{item.quantity}</strong>
//                     </td>

//                     <td>{item.unit}</td>

//                     <td>{item.minimum_stock}</td>

//                     <td>
//                       {isLowStock ? (
//                         <span className="status low">
//                           ⚠ Low Stock
//                         </span>
//                       ) : (
//                         <span className="status healthy">
//                           ✓ Healthy
//                         </span>
//                       )}
//                     </td>

//                   </tr>
//                 );
//               })}
//             </tbody>

//           </table>

//         </div>
//       )}

//     </main>
//   );
// }

// export default Inventory;


// import { useEffect, useState } from "react";
// import "./Inventory.css";

// interface InventoryItem {
//   _id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   minimum_stock: number;
//   supplier_id?: string;
// }

// interface InventoryResponse {
//   status: string;
//   count: number;
//   inventory: InventoryItem[];
// }

// function Inventory() {
//   const [inventory, setInventory] = useState<InventoryItem[]>([]);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState("");

//   const [showForm, setShowForm] = useState(false);

//   const [ingredientName, setIngredientName] = useState("");
//   const [quantity, setQuantity] = useState("");
//   const [unit, setUnit] = useState("");
//   const [minimumStock, setMinimumStock] = useState("");
  

//   // ==============================
//   // GET INVENTORY
//   // ==============================

//   const fetchInventory = () => {
//     setLoading(true);

//     fetch("http://127.0.0.1:8000/inventory/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch inventory");
//         }

//         return response.json();
//       })
//       .then((data: InventoryResponse) => {
//         setInventory(data.inventory);
//         setLoading(false);
//       })
//       .catch((error) => {
//         console.error("Inventory API Error:", error);
//         setError("Unable to load inventory");
//         setLoading(false);
//       });
//   };

//   useEffect(() => {
//     fetchInventory();
//   }, []);

//   // ==============================
//   // ADD INVENTORY
//   // ==============================

//   const handleAddInventory = async (
//     event: React.FormEvent<HTMLFormElement>
//   ) => {
//     event.preventDefault();

//     try {
//       const response = await fetch(
//         "http://127.0.0.1:8000/inventory/",
//         {
//           method: "POST",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({
//             ingredient_name: ingredientName,
//             quantity: Number(quantity),
//             unit: unit,
//             minimum_stock: Number(minimumStock),
//           }),
//         }
//       );

//       const data = await response.json();

//       if (!response.ok) {
//         console.error("Add Inventory Error:", data);
//         alert("Failed to add inventory");
//         return;
//       }

//       alert("Inventory added successfully!");

//       // Clear form
//       setIngredientName("");
//       setQuantity("");
//       setUnit("");
//       setMinimumStock("");

//       // Close form
//       setShowForm(false);

//       // Refresh inventory
//       fetchInventory();

//     } catch (error) {
//       console.error("Error:", error);
//       alert("Unable to connect to backend");
//     }
//   };

//   return (
//     <main className="inventory-page">

//       {/* ==============================
//           PAGE HEADER
//       ============================== */}

//       <div className="inventory-header">

//         <div>
//           <p className="inventory-welcome">
//             Inventory Management
//           </p>

//           <h1>Inventory</h1>

//           <span>
//             Manage your restaurant ingredients and stock levels
//           </span>
//         </div>

//         <button
//           className="add-inventory-btn"
//           onClick={() => setShowForm(!showForm)}
//         >
//           + Add Inventory
//         </button>

//       </div>


//       {/* ==============================
//           ADD INVENTORY FORM
//       ============================== */}

//       {showForm && (
//         <div className="inventory-form-container">

//           <h2>Add Inventory</h2>

//           <form onSubmit={handleAddInventory}>

//             <div className="form-group">

//               <label>Ingredient Name</label>

//               <input
//                 type="text"
//                 placeholder="Example: Tomato"
//                 value={ingredientName}
//                 onChange={(event) =>
//                   setIngredientName(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-group">

//               <label>Quantity</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 20"
//                 value={quantity}
//                 onChange={(event) =>
//                   setQuantity(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-group">

//               <label>Unit</label>

//               <select
//                 value={unit}
//                 onChange={(event) =>
//                   setUnit(event.target.value)
//                 }
//                 required
//               >

//                 <option value="">
//                   Select Unit
//                 </option>

//                 <option value="kg">
//                   kg
//                 </option>

//                 <option value="g">
//                   g
//                 </option>

//                 <option value="liter">
//                   liter
//                 </option>

//                 <option value="ml">
//                   ml
//                 </option>

//                 <option value="piece">
//                   piece
//                 </option>

//               </select>

//             </div>


//             <div className="form-group">

//               <label>Minimum Stock</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 10"
//                 value={minimumStock}
//                 onChange={(event) =>
//                   setMinimumStock(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-buttons">

//               <button
//                 type="submit"
//                 className="save-btn"
//               >
//                 Save Inventory
//               </button>

//               <button
//                 type="button"
//                 className="cancel-btn"
//                 onClick={() => setShowForm(false)}
//               >
//                 Cancel
//               </button>

//             </div>

//           </form>

//         </div>
//       )}


//       {/* ==============================
//           LOADING
//       ============================== */}

//       {loading && (
//         <div className="inventory-message">
//           Loading inventory...
//         </div>
//       )}


//       {/* ==============================
//           ERROR
//       ============================== */}

//       {error && (
//         <div className="inventory-error">
//           {error}
//         </div>
//       )}


//       {/* ==============================
//           INVENTORY TABLE
//       ============================== */}

//       {!loading && !error && (

//         <div className="inventory-table-container">

//           <table className="inventory-table">

//             <thead>

//               <tr>
//                 <th>Ingredient</th>
//                 <th>Quantity</th>
//                 <th>Unit</th>
//                 <th>Minimum Stock</th>
//                 <th>Status</th>
//               </tr>

//             </thead>


//             <tbody>

//               {inventory.map((item) => {

//                 const isLowStock =
//                   item.quantity <= item.minimum_stock;

//                 return (

//                   <tr key={item._id}>

//                     <td>
//                       <div className="ingredient-name">
//                         🥕 {item.ingredient_name}
//                       </div>
//                     </td>

//                     <td>
//                       <strong>
//                         {item.quantity}
//                       </strong>
//                     </td>

//                     <td>
//                       {item.unit}
//                     </td>

//                     <td>
//                       {item.minimum_stock}
//                     </td>

//                     <td>

//                       {isLowStock ? (

//                         <span className="status low">
//                           ⚠ Low Stock
//                         </span>

//                       ) : (

//                         <span className="status healthy">
//                           ✓ Healthy
//                         </span>

//                       )}

//                     </td>

//                   </tr>

//                 );

//               })}

//             </tbody>

//           </table>

//         </div>

//       )}

//     </main>
//   );
// }

// export default Inventory;

// import { useEffect, useState } from "react";
// import "./Inventory.css";

// interface InventoryItem {
//   _id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   minimum_stock: number;
//   supplier_id?: string;
// }

// interface InventoryResponse {
//   status: string;
//   count: number;
//   inventory: InventoryItem[];
// }

// function Inventory() {
//   const [inventory, setInventory] = useState<InventoryItem[]>([]);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState("");

//   // ==============================
//   // ADD INVENTORY
//   // ==============================

//   const [showForm, setShowForm] = useState(false);

//   const [ingredientName, setIngredientName] = useState("");
//   const [quantity, setQuantity] = useState("");
//   const [unit, setUnit] = useState("");
//   const [minimumStock, setMinimumStock] = useState("");

//   // ==============================
//   // EDIT INVENTORY
//   // ==============================

//   const [editingItem, setEditingItem] =
//     useState<InventoryItem | null>(null);

//   const [editIngredientName, setEditIngredientName] = useState("");
//   const [editQuantity, setEditQuantity] = useState("");
//   const [editUnit, setEditUnit] = useState("");
//   const [editMinimumStock, setEditMinimumStock] = useState("");

//   // ==============================
//   // GET INVENTORY
//   // ==============================

//   const fetchInventory = () => {
//     setLoading(true);

//     fetch("http://127.0.0.1:8000/inventory/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch inventory");
//         }

//         return response.json();
//       })
//       .then((data: InventoryResponse) => {
//         setInventory(data.inventory);
//         setLoading(false);
//         setError("");
//       })
//       .catch((error) => {
//         console.error("Inventory API Error:", error);
//         setError("Unable to load inventory");
//         setLoading(false);
//       });
//   };

//   useEffect(() => {
//     fetchInventory();
//   }, []);

//   // ==============================
//   // ADD INVENTORY
//   // ==============================

//   const handleAddInventory = async (
//     event: React.FormEvent<HTMLFormElement>
//   ) => {
//     event.preventDefault();

//     try {
//       const response = await fetch(
//         "http://127.0.0.1:8000/inventory/",
//         {
//           method: "POST",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({
//             ingredient_name: ingredientName,
//             quantity: Number(quantity),
//             unit: unit,
//             minimum_stock: Number(minimumStock),
//           }),
//         }
//       );

//       const data = await response.json();

//       if (!response.ok) {
//         console.error("Add Inventory Error:", data);
//         alert("Failed to add inventory");
//         return;
//       }

//       alert("Inventory added successfully!");

//       // Clear form
//       setIngredientName("");
//       setQuantity("");
//       setUnit("");
//       setMinimumStock("");

//       // Close form
//       setShowForm(false);

//       // Refresh inventory
//       fetchInventory();

//     } catch (error) {
//       console.error("Error:", error);
//       alert("Unable to connect to backend");
//     }
//   };

//   // ==============================
//   // START EDIT INVENTORY
//   // ==============================

//   const handleEditClick = (item: InventoryItem) => {
//     setEditingItem(item);

//     setEditIngredientName(item.ingredient_name);
//     setEditQuantity(String(item.quantity));
//     setEditUnit(item.unit);
//     setEditMinimumStock(String(item.minimum_stock));

//     // Close Add form if it is open
//     setShowForm(false);
//   };

//   // ==============================
//   // UPDATE INVENTORY
//   // ==============================

//   const handleUpdateInventory = async (
//     event: React.FormEvent<HTMLFormElement>
//   ) => {
//     event.preventDefault();

//     if (!editingItem) {
//       return;
//     }

//     try {
//       const response = await fetch(
//         `http://127.0.0.1:8000/inventory/${editingItem._id}`,
//         {
//           method: "PUT",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({
//             ingredient_name: editIngredientName,
//             quantity: Number(editQuantity),
//             unit: editUnit,
//             minimum_stock: Number(editMinimumStock),
//           }),
//         }
//       );

//       const data = await response.json();

//       if (!response.ok) {
//         console.error("Update Inventory Error:", data);
//         alert("Failed to update inventory");
//         return;
//       }

//       alert("Inventory updated successfully!");

//       // Clear edit form
//       setEditingItem(null);
//       setEditIngredientName("");
//       setEditQuantity("");
//       setEditUnit("");
//       setEditMinimumStock("");

//       // Refresh inventory
//       fetchInventory();

//     } catch (error) {
//       console.error("Error:", error);
//       alert("Unable to connect to backend");
//     }
//   };

//   // ==============================
//   // CANCEL EDIT
//   // ==============================

//   const handleCancelEdit = () => {
//     setEditingItem(null);

//     setEditIngredientName("");
//     setEditQuantity("");
//     setEditUnit("");
//     setEditMinimumStock("");
//   };

//   return (
//     <main className="inventory-page">

//       {/* ==============================
//           PAGE HEADER
//       ============================== */}

//       <div className="inventory-header">

//         <div>
//           <p className="inventory-welcome">
//             Inventory Management
//           </p>

//           <h1>Inventory</h1>

//           <span>
//             Manage your restaurant ingredients and stock levels
//           </span>
//         </div>

//         <button
//           className="add-inventory-btn"
//           onClick={() => {
//             setShowForm(!showForm);
//             setEditingItem(null);
//           }}
//         >
//           + Add Inventory
//         </button>

//       </div>


//       {/* ==============================
//           ADD INVENTORY FORM
//       ============================== */}

//       {showForm && (
//         <div className="inventory-form-container">

//           <h2>Add Inventory</h2>

//           <form onSubmit={handleAddInventory}>

//             <div className="form-group">

//               <label>Ingredient Name</label>

//               <input
//                 type="text"
//                 placeholder="Example: Tomato"
//                 value={ingredientName}
//                 onChange={(event) =>
//                   setIngredientName(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-group">

//               <label>Quantity</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 20"
//                 value={quantity}
//                 onChange={(event) =>
//                   setQuantity(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-group">

//               <label>Unit</label>

//               <select
//                 value={unit}
//                 onChange={(event) =>
//                   setUnit(event.target.value)
//                 }
//                 required
//               >

//                 <option value="">
//                   Select Unit
//                 </option>

//                 <option value="kg">
//                   kg
//                 </option>

//                 <option value="g">
//                   g
//                 </option>

//                 <option value="liter">
//                   liter
//                 </option>

//                 <option value="ml">
//                   ml
//                 </option>

//                 <option value="piece">
//                   piece
//                 </option>

//               </select>

//             </div>


//             <div className="form-group">

//               <label>Minimum Stock</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 10"
//                 value={minimumStock}
//                 onChange={(event) =>
//                   setMinimumStock(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-buttons">

//               <button
//                 type="submit"
//                 className="save-btn"
//               >
//                 Save Inventory
//               </button>

//               <button
//                 type="button"
//                 className="cancel-btn"
//                 onClick={() => setShowForm(false)}
//               >
//                 Cancel
//               </button>

//             </div>

//           </form>

//         </div>
//       )}


//       {/* ==============================
//           EDIT INVENTORY FORM
//       ============================== */}

//       {editingItem && (
//         <div className="inventory-form-container edit-form">

//           <h2>Edit Inventory</h2>

//           <p className="editing-name">
//             Editing: <strong>{editingItem.ingredient_name}</strong>
//           </p>

//           <form onSubmit={handleUpdateInventory}>

//             <div className="form-group">

//               <label>Ingredient Name</label>

//               <input
//                 type="text"
//                 placeholder="Example: Tomato"
//                 value={editIngredientName}
//                 onChange={(event) =>
//                   setEditIngredientName(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-group">

//               <label>Quantity</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 20"
//                 value={editQuantity}
//                 onChange={(event) =>
//                   setEditQuantity(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-group">

//               <label>Unit</label>

//               <select
//                 value={editUnit}
//                 onChange={(event) =>
//                   setEditUnit(event.target.value)
//                 }
//                 required
//               >

//                 <option value="">
//                   Select Unit
//                 </option>

//                 <option value="kg">
//                   kg
//                 </option>

//                 <option value="g">
//                   g
//                 </option>

//                 <option value="liter">
//                   liter
//                 </option>

//                 <option value="ml">
//                   ml
//                 </option>

//                 <option value="piece">
//                   piece
//                 </option>

//               </select>

//             </div>


//             <div className="form-group">

//               <label>Minimum Stock</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 10"
//                 value={editMinimumStock}
//                 onChange={(event) =>
//                   setEditMinimumStock(event.target.value)
//                 }
//                 required
//               />

//             </div>


//             <div className="form-buttons">

//               <button
//                 type="submit"
//                 className="save-btn"
//               >
//                 Update Inventory
//               </button>

//               <button
//                 type="button"
//                 className="cancel-btn"
//                 onClick={handleCancelEdit}
//               >
//                 Cancel
//               </button>

//             </div>

//           </form>

//         </div>
//       )}


//       {/* ==============================
//           LOADING
//       ============================== */}

//       {loading && (
//         <div className="inventory-message">
//           Loading inventory...
//         </div>
//       )}


//       {/* ==============================
//           ERROR
//       ============================== */}

//       {error && (
//         <div className="inventory-error">
//           {error}
//         </div>
//       )}


//       {/* ==============================
//           INVENTORY TABLE
//       ============================== */}

//       {!loading && !error && (

//         <div className="inventory-table-container">

//           <table className="inventory-table">

//             <thead>

//               <tr>
//                 <th>Ingredient</th>
//                 <th>Quantity</th>
//                 <th>Unit</th>
//                 <th>Minimum Stock</th>
//                 <th>Status</th>
//                 <th>Action</th>
//               </tr>

//             </thead>


//             <tbody>

//               {inventory.map((item) => {

//                 const isLowStock =
//                   item.quantity <= item.minimum_stock;

//                 return (

//                   <tr key={item._id}>

//                     <td>
//                       <div className="ingredient-name">
//                         🥕 {item.ingredient_name}
//                       </div>
//                     </td>

//                     <td>
//                       <strong>
//                         {item.quantity}
//                       </strong>
//                     </td>

//                     <td>
//                       {item.unit}
//                     </td>

//                     <td>
//                       {item.minimum_stock}
//                     </td>

//                     <td>

//                       {isLowStock ? (

//                         <span className="status low">
//                           ⚠ Low Stock
//                         </span>

//                       ) : (

//                         <span className="status healthy">
//                           ✓ Healthy
//                         </span>

//                       )}

//                     </td>

//                     <td>
//                       <button
//                         className="edit-btn"
//                         onClick={() =>
//                           handleEditClick(item)
//                         }
//                       >
//                         ✏ Edit
//                       </button>
//                     </td>

//                   </tr>

//                 );

//               })}

//             </tbody>

//           </table>

//         </div>

//       )}

//     </main>
//   );
// }

// export default Inventory;

// import { useEffect, useState } from "react";
// import "./Inventory.css";

// interface InventoryItem {
//   _id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   minimum_stock: number;
//   supplier_id?: string;
// }

// interface InventoryResponse {
//   status: string;
//   count: number;
//   inventory: InventoryItem[];
// }

// function Inventory() {
//   const [inventory, setInventory] = useState<InventoryItem[]>([]);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState("");

//   // =========================
//   // ADD INVENTORY
//   // =========================
//   const [showForm, setShowForm] = useState(false);
//   const [ingredientName, setIngredientName] = useState("");
//   const [quantity, setQuantity] = useState("");
//   const [unit, setUnit] = useState("");
//   const [minimumStock, setMinimumStock] = useState("");

//   // =========================
//   // EDIT INVENTORY
//   // =========================
//   const [editingItem, setEditingItem] =
//     useState<InventoryItem | null>(null);

//   const [editIngredientName, setEditIngredientName] = useState("");
//   const [editQuantity, setEditQuantity] = useState("");
//   const [editUnit, setEditUnit] = useState("");
//   const [editMinimumStock, setEditMinimumStock] = useState("");



//   const [lowStockItems, setLowStockItems] = useState<InventoryItem[]>([]);
// const [lowStockLoading, setLowStockLoading] = useState(false);


//   // =========================
//   // GET INVENTORY
//   // =========================
//   const fetchInventory = () => {
//     setLoading(true);

//     fetch("http://127.0.0.1:8000/inventory/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch inventory");
//         }

//         return response.json();
//       })
//       .then((data: InventoryResponse) => {
//         setInventory(data.inventory);
//         setLoading(false);
//         setError("");
//       })
//       .catch((error) => {
//         console.error("Inventory API Error:", error);
//         setError("Unable to load inventory");
//         setLoading(false);
//       });
//   };

//   useEffect(() => {
//     fetchInventory();
//   }, []);

//   // =========================
//   // ADD INVENTORY
//   // =========================
//   const handleAddInventory = async (
//     event: React.FormEvent<HTMLFormElement>
//   ) => {
//     event.preventDefault();

//     try {
//       const response = await fetch(
//         "http://127.0.0.1:8000/inventory/",
//         {
//           method: "POST",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({
//             ingredient_name: ingredientName,
//             quantity: Number(quantity),
//             unit: unit,
//             minimum_stock: Number(minimumStock),
//           }),
//         }
//       );

//       const data = await response.json();

//       if (!response.ok) {
//         console.error("Add Inventory Error:", data);
//         alert("Failed to add inventory");
//         return;
//       }

//       alert("Inventory added successfully!");

//       setIngredientName("");
//       setQuantity("");
//       setUnit("");
//       setMinimumStock("");

//       setShowForm(false);

//       fetchInventory();
//     } catch (error) {
//       console.error("Error:", error);
//       alert("Unable to connect to backend");
//     }
//   };

//   // =========================
//   // EDIT BUTTON
//   // =========================
//   const handleEditClick = (item: InventoryItem) => {
//     setEditingItem(item);

//     setEditIngredientName(item.ingredient_name);
//     setEditQuantity(String(item.quantity));
//     setEditUnit(item.unit);
//     setEditMinimumStock(String(item.minimum_stock));

//     setShowForm(false);
//   };

//   // =========================
//   // UPDATE INVENTORY
//   // =========================
//   const handleUpdateInventory = async (
//     event: React.FormEvent<HTMLFormElement>
//   ) => {
//     event.preventDefault();

//     if (!editingItem) return;

//     try {
//       const response = await fetch(
//         `http://127.0.0.1:8000/inventory/${editingItem._id}`,
//         {
//           method: "PUT",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({
//             ingredient_name: editIngredientName,
//             quantity: Number(editQuantity),
//             unit: editUnit,
//             minimum_stock: Number(editMinimumStock),
//           }),
//         }
//       );

//       const data = await response.json();

//       if (!response.ok) {
//         console.error("Update Inventory Error:", data);
//         alert("Failed to update inventory");
//         return;
//       }

//       alert("Inventory updated successfully!");

//       setEditingItem(null);

//       setEditIngredientName("");
//       setEditQuantity("");
//       setEditUnit("");
//       setEditMinimumStock("");

//       fetchInventory();
//     } catch (error) {
//       console.error("Error:", error);
//       alert("Unable to connect to backend");
//     }
//   };

//   // =========================
//   // CANCEL EDIT
//   // =========================
//   const handleCancelEdit = () => {
//     setEditingItem(null);

//     setEditIngredientName("");
//     setEditQuantity("");
//     setEditUnit("");
//     setEditMinimumStock("");
//   };

//   // =========================
//   // DELETE INVENTORY
//   // =========================
//   const handleDeleteInventory = async (
//     item: InventoryItem
//   ) => {
//     const confirmDelete = window.confirm(
//       `Are you sure you want to delete "${item.ingredient_name}"?`
//     );

//     if (!confirmDelete) {
//       return;
//     }

//     try {
//       const response = await fetch(
//         `http://127.0.0.1:8000/inventory/${item._id}`,
//         {
//           method: "DELETE",
//         }
//       );

//       const data = await response.json();

//       if (!response.ok) {
//         console.error("Delete Inventory Error:", data);
//         alert("Failed to delete inventory");
//         return;
//       }

//       alert("Inventory deleted successfully!");

//       // Refresh inventory list
//       fetchInventory();
//     } catch (error) {
//       console.error("Error:", error);
//       alert("Unable to connect to backend");
//     }
//   };

//   return (
//     <main className="inventory-page">

//       {/* =========================
//           HEADER
//       ========================= */}
//       <div className="inventory-header">
//         <div>
//           <p className="inventory-welcome">
//             Inventory Management
//           </p>

//           <h1>Inventory</h1>

//           <span>
//             Manage your restaurant ingredients and stock levels
//           </span>
//         </div>

//         <button
//           className="add-inventory-btn"
//           onClick={() => {
//             setShowForm(!showForm);
//             setEditingItem(null);
//           }}
//         >
//           + Add Inventory
//         </button>
//       </div>

//       {/* =========================
//           ADD INVENTORY FORM
//       ========================= */}
//       {showForm && (
//         <div className="inventory-form-container">

//           <h2>Add Inventory</h2>

//           <form onSubmit={handleAddInventory}>

//             <div className="form-group">
//               <label>Ingredient Name</label>

//               <input
//                 type="text"
//                 placeholder="Example: Tomato"
//                 value={ingredientName}
//                 onChange={(event) =>
//                   setIngredientName(event.target.value)
//                 }
//                 required
//               />
//             </div>

//             <div className="form-group">
//               <label>Quantity</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 20"
//                 value={quantity}
//                 onChange={(event) =>
//                   setQuantity(event.target.value)
//                 }
//                 required
//               />
//             </div>

//             <div className="form-group">
//               <label>Unit</label>

//               <select
//                 value={unit}
//                 onChange={(event) =>
//                   setUnit(event.target.value)
//                 }
//                 required
//               >
//                 <option value="">
//                   Select Unit
//                 </option>

//                 <option value="kg">
//                   kg
//                 </option>

//                 <option value="g">
//                   g
//                 </option>

//                 <option value="liter">
//                   liter
//                 </option>

//                 <option value="ml">
//                   ml
//                 </option>

//                 <option value="piece">
//                   piece
//                 </option>
//               </select>
//             </div>

//             <div className="form-group">
//               <label>Minimum Stock</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 10"
//                 value={minimumStock}
//                 onChange={(event) =>
//                   setMinimumStock(event.target.value)
//                 }
//                 required
//               />
//             </div>

//             <div className="form-buttons">

//               <button
//                 type="submit"
//                 className="save-btn"
//               >
//                 Save Inventory
//               </button>

//               <button
//                 type="button"
//                 className="cancel-btn"
//                 onClick={() => setShowForm(false)}
//               >
//                 Cancel
//               </button>

//             </div>
//           </form>
//         </div>
//       )}

//       {/* =========================
//           EDIT INVENTORY FORM
//       ========================= */}
//       {editingItem && (
//         <div className="inventory-form-container edit-form">

//           <h2>Edit Inventory</h2>

//           <p className="editing-name">
//             Editing:{" "}
//             <strong>
//               {editingItem.ingredient_name}
//             </strong>
//           </p>

//           <form onSubmit={handleUpdateInventory}>

//             <div className="form-group">
//               <label>Ingredient Name</label>

//               <input
//                 type="text"
//                 placeholder="Example: Tomato"
//                 value={editIngredientName}
//                 onChange={(event) =>
//                   setEditIngredientName(event.target.value)
//                 }
//                 required
//               />
//             </div>

//             <div className="form-group">
//               <label>Quantity</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 20"
//                 value={editQuantity}
//                 onChange={(event) =>
//                   setEditQuantity(event.target.value)
//                 }
//                 required
//               />
//             </div>

//             <div className="form-group">
//               <label>Unit</label>

//               <select
//                 value={editUnit}
//                 onChange={(event) =>
//                   setEditUnit(event.target.value)
//                 }
//                 required
//               >
//                 <option value="">
//                   Select Unit
//                 </option>

//                 <option value="kg">
//                   kg
//                 </option>

//                 <option value="g">
//                   g
//                 </option>

//                 <option value="liter">
//                   liter
//                 </option>

//                 <option value="ml">
//                   ml
//                 </option>

//                 <option value="piece">
//                   piece
//                 </option>
//               </select>
//             </div>

//             <div className="form-group">
//               <label>Minimum Stock</label>

//               <input
//                 type="number"
//                 min="0"
//                 placeholder="Example: 10"
//                 value={editMinimumStock}
//                 onChange={(event) =>
//                   setEditMinimumStock(event.target.value)
//                 }
//                 required
//               />
//             </div>

//             <div className="form-buttons">

//               <button
//                 type="submit"
//                 className="save-btn"
//               >
//                 Update Inventory
//               </button>

//               <button
//                 type="button"
//                 className="cancel-btn"
//                 onClick={handleCancelEdit}
//               >
//                 Cancel
//               </button>

//             </div>
//           </form>
//         </div>
//       )}

//       {/* =========================
//           LOADING
//       ========================= */}
//       {loading && (
//         <div className="inventory-message">
//           Loading inventory...
//         </div>
//       )}

//       {/* =========================
//           ERROR
//       ========================= */}
//       {error && (
//         <div className="inventory-error">
//           {error}
//         </div>
//       )}

//       {/* =========================
//           INVENTORY TABLE
//       ========================= */}
//       {!loading && !error && (
//         <div className="inventory-table-container">

//           <table className="inventory-table">

//             <thead>
//               <tr>
//                 <th>Ingredient</th>
//                 <th>Quantity</th>
//                 <th>Unit</th>
//                 <th>Minimum Stock</th>
//                 <th>Status</th>
//                 <th>Action</th>
//               </tr>
//             </thead>

//             <tbody>

//               {inventory.map((item) => {

//                 const isLowStock =
//                   item.quantity <= item.minimum_stock;

//                 return (
//                   <tr key={item._id}>

//                     <td>
//                       <div className="ingredient-name">
//                         🥕 {item.ingredient_name}
//                       </div>
//                     </td>

//                     <td>
//                       <strong>
//                         {item.quantity}
//                       </strong>
//                     </td>

//                     <td>
//                       {item.unit}
//                     </td>

//                     <td>
//                       {item.minimum_stock}
//                     </td>

//                     <td>

//                       {isLowStock ? (
//                         <span className="status low">
//                           ⚠ Low Stock
//                         </span>
//                       ) : (
//                         <span className="status healthy">
//                           ✓ Healthy
//                         </span>
//                       )}

//                     </td>

//                     <td>

//                       <div className="action-buttons">

//                         <button
//                           className="edit-btn"
//                           onClick={() =>
//                             handleEditClick(item)
//                           }
//                         >
//                           ✏ Edit
//                         </button>

//                         <button
//                           className="delete-btn"
//                           onClick={() =>
//                             handleDeleteInventory(item)
//                           }
//                         >
//                           🗑 Delete
//                         </button>

//                       </div>

//                     </td>

//                   </tr>
//                 );
//               })}

//             </tbody>
//           </table>
//         </div>
//       )}

//     </main>
//   );
// }

// export default Inventory;


import { useEffect, useState } from "react";
import "./Inventory.css";

interface InventoryItem {
  _id: string;
  ingredient_name: string;
  quantity: number;
  unit: string;
  minimum_stock: number;
  supplier_id?: string;
}

interface InventoryResponse {
  status: string;
  count: number;
  inventory: InventoryItem[];
}

interface LowStockResponse {
  status: string;
  count: number;
  low_stock: InventoryItem[];
}

function Inventory() {
  const [inventory, setInventory] = useState<InventoryItem[]>([]);
  const [lowStockItems, setLowStockItems] = useState<InventoryItem[]>([]);

  const [loading, setLoading] = useState(true);
  const [lowStockLoading, setLowStockLoading] = useState(false);
  const [error, setError] = useState("");

  // ADD INVENTORY
  const [showForm, setShowForm] = useState(false);
  const [ingredientName, setIngredientName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [unit, setUnit] = useState("");
  const [minimumStock, setMinimumStock] = useState("");

  // EDIT INVENTORY
  const [editingItem, setEditingItem] = useState<InventoryItem | null>(null);
  const [editIngredientName, setEditIngredientName] = useState("");
  const [editQuantity, setEditQuantity] = useState("");
  const [editUnit, setEditUnit] = useState("");
  const [editMinimumStock, setEditMinimumStock] = useState("");

  // ==============================
  // GET ALL INVENTORY
  // ==============================
  const fetchInventory = () => {
    setLoading(true);

    fetch("http://127.0.0.1:8000/inventory/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch inventory");
        }

        return response.json();
      })
      .then((data: InventoryResponse) => {
        setInventory(data.inventory);
        setLoading(false);
        setError("");
      })
      .catch((error) => {
        console.error("Inventory API Error:", error);
        setError("Unable to load inventory");
        setLoading(false);
      });
  };

  // ==============================
  // GET LOW STOCK
  // ==============================
  const fetchLowStock = () => {
    setLowStockLoading(true);

    fetch("http://127.0.0.1:8000/inventory/low-stock")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch low stock");
        }

        return response.json();
      })
      .then((data: LowStockResponse) => {
        setLowStockItems(data.low_stock);
        setLowStockLoading(false);
      })
      .catch((error) => {
        console.error("Low Stock API Error:", error);
        setLowStockLoading(false);
      });
  };

  // ==============================
  // LOAD DATA
  // ==============================
  useEffect(() => {
    fetchInventory();
    fetchLowStock();
  }, []);

  // ==============================
  // ADD INVENTORY
  // ==============================
  const handleAddInventory = async (
    event: React.FormEvent<HTMLFormElement>
  ) => {
    event.preventDefault();

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/inventory/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ingredient_name: ingredientName,
            quantity: Number(quantity),
            unit: unit,
            minimum_stock: Number(minimumStock),
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        console.error("Add Inventory Error:", data);
        alert("Failed to add inventory");
        return;
      }

      alert("Inventory added successfully!");

      setIngredientName("");
      setQuantity("");
      setUnit("");
      setMinimumStock("");
      setShowForm(false);

      fetchInventory();
      fetchLowStock();
    } catch (error) {
      console.error("Error:", error);
      alert("Unable to connect to backend");
    }
  };

  // ==============================
  // EDIT BUTTON
  // ==============================
  const handleEditClick = (item: InventoryItem) => {
    setEditingItem(item);

    setEditIngredientName(item.ingredient_name);
    setEditQuantity(String(item.quantity));
    setEditUnit(item.unit);
    setEditMinimumStock(String(item.minimum_stock));

    setShowForm(false);
  };

  // ==============================
  // UPDATE INVENTORY
  // ==============================
  const handleUpdateInventory = async (
    event: React.FormEvent<HTMLFormElement>
  ) => {
    event.preventDefault();

    if (!editingItem) return;

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/inventory/${editingItem._id}`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ingredient_name: editIngredientName,
            quantity: Number(editQuantity),
            unit: editUnit,
            minimum_stock: Number(editMinimumStock),
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        console.error("Update Inventory Error:", data);
        alert("Failed to update inventory");
        return;
      }

      alert("Inventory updated successfully!");

      setEditingItem(null);
      setEditIngredientName("");
      setEditQuantity("");
      setEditUnit("");
      setEditMinimumStock("");

      fetchInventory();
      fetchLowStock();
    } catch (error) {
      console.error("Error:", error);
      alert("Unable to connect to backend");
    }
  };

  // ==============================
  // CANCEL EDIT
  // ==============================
  const handleCancelEdit = () => {
    setEditingItem(null);

    setEditIngredientName("");
    setEditQuantity("");
    setEditUnit("");
    setEditMinimumStock("");
  };

  // ==============================
  // DELETE INVENTORY
  // ==============================
  const handleDeleteInventory = async (item: InventoryItem) => {
    const confirmDelete = window.confirm(
      `Are you sure you want to delete "${item.ingredient_name}"?`
    );

    if (!confirmDelete) return;

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/inventory/${item._id}`,
        {
          method: "DELETE",
        }
      );

      const data = await response.json();

      if (!response.ok) {
        console.error("Delete Inventory Error:", data);
        alert("Failed to delete inventory");
        return;
      }

      alert("Inventory deleted successfully!");

      fetchInventory();
      fetchLowStock();
    } catch (error) {
      console.error("Error:", error);
      alert("Unable to connect to backend");
    }
  };

  return (
    <main className="inventory-page">

      {/* ==============================
          HEADER
      ============================== */}
      <div className="inventory-header">
        <div>
          <p className="inventory-welcome">
            Inventory Management
          </p>

          <h1>Inventory</h1>

          <span>
            Manage your restaurant ingredients and stock levels
          </span>
        </div>

        <button
          className="add-inventory-btn"
          onClick={() => {
            setShowForm(!showForm);
            setEditingItem(null);
          }}
        >
          + Add Inventory
        </button>
      </div>

      {/* ==============================
          ADD FORM
      ============================== */}
      {showForm && (
        <div className="inventory-form-container">
          <h2>Add Inventory</h2>

          <form onSubmit={handleAddInventory}>

            <div className="form-group">
              <label>Ingredient Name</label>

              <input
                type="text"
                placeholder="Example: Tomato"
                value={ingredientName}
                onChange={(event) =>
                  setIngredientName(event.target.value)
                }
                required
              />
            </div>

            <div className="form-group">
              <label>Quantity</label>

              <input
                type="number"
                min="0"
                placeholder="Example: 20"
                value={quantity}
                onChange={(event) =>
                  setQuantity(event.target.value)
                }
                required
              />
            </div>

            <div className="form-group">
              <label>Unit</label>

              <select
                value={unit}
                onChange={(event) =>
                  setUnit(event.target.value)
                }
                required
              >
                <option value="">Select Unit</option>
                <option value="kg">kg</option>
                <option value="g">g</option>
                <option value="liter">liter</option>
                <option value="ml">ml</option>
                <option value="piece">piece</option>
              </select>
            </div>

            <div className="form-group">
              <label>Minimum Stock</label>

              <input
                type="number"
                min="0"
                placeholder="Example: 10"
                value={minimumStock}
                onChange={(event) =>
                  setMinimumStock(event.target.value)
                }
                required
              />
            </div>

            <div className="form-buttons">
              <button
                type="submit"
                className="save-btn"
              >
                Save Inventory
              </button>

              <button
                type="button"
                className="cancel-btn"
                onClick={() => setShowForm(false)}
              >
                Cancel
              </button>
            </div>

          </form>
        </div>
      )}

      {/* ==============================
          EDIT FORM
      ============================== */}
      {editingItem && (
        <div className="inventory-form-container edit-form">

          <h2>Edit Inventory</h2>

          <p className="editing-name">
            Editing:{" "}
            <strong>
              {editingItem.ingredient_name}
            </strong>
          </p>

          <form onSubmit={handleUpdateInventory}>

            <div className="form-group">
              <label>Ingredient Name</label>

              <input
                type="text"
                placeholder="Example: Tomato"
                value={editIngredientName}
                onChange={(event) =>
                  setEditIngredientName(event.target.value)
                }
                required
              />
            </div>

            <div className="form-group">
              <label>Quantity</label>

              <input
                type="number"
                min="0"
                placeholder="Example: 20"
                value={editQuantity}
                onChange={(event) =>
                  setEditQuantity(event.target.value)
                }
                required
              />
            </div>

            <div className="form-group">
              <label>Unit</label>

              <select
                value={editUnit}
                onChange={(event) =>
                  setEditUnit(event.target.value)
                }
                required
              >
                <option value="">Select Unit</option>
                <option value="kg">kg</option>
                <option value="g">g</option>
                <option value="liter">liter</option>
                <option value="ml">ml</option>
                <option value="piece">piece</option>
              </select>
            </div>

            <div className="form-group">
              <label>Minimum Stock</label>

              <input
                type="number"
                min="0"
                placeholder="Example: 10"
                value={editMinimumStock}
                onChange={(event) =>
                  setEditMinimumStock(event.target.value)
                }
                required
              />
            </div>

            <div className="form-buttons">

              <button
                type="submit"
                className="save-btn"
              >
                Update Inventory
              </button>

              <button
                type="button"
                className="cancel-btn"
                onClick={handleCancelEdit}
              >
                Cancel
              </button>

            </div>

          </form>
        </div>
      )}

      {/* ==============================
          LOW STOCK ALERT
      ============================== */}
      {!lowStockLoading && lowStockItems.length > 0 && (
        <div className="low-stock-container">

          <div className="low-stock-header">

            <div>
              <h2>⚠ Low Stock Alert</h2>

              <p>
                These ingredients need attention.
              </p>
            </div>

            <span className="low-stock-count">
              {lowStockItems.length} Items
            </span>

          </div>

          <div className="low-stock-list">

            {lowStockItems.map((item) => (
              <div
                className="low-stock-item"
                key={item._id}
              >

                <div className="low-stock-info">

                  <div className="low-stock-name">
                    🥕 {item.ingredient_name}
                  </div>

                  <div className="low-stock-details">
                    Current Stock:{" "}
                    <strong>
                      {item.quantity} {item.unit}
                    </strong>

                    {" • "}

                    Minimum Required:{" "}
                    <strong>
                      {item.minimum_stock} {item.unit}
                    </strong>
                  </div>

                </div>

                <span className="low-stock-badge">
                  ⚠ Low Stock
                </span>

              </div>
            ))}

          </div>
        </div>
      )}

      {/* ==============================
          LOADING
      ============================== */}
      {loading && (
        <div className="inventory-message">
          Loading inventory...
        </div>
      )}

      {/* ==============================
          ERROR
      ============================== */}
      {error && (
        <div className="inventory-error">
          {error}
        </div>
      )}

      {/* ==============================
          INVENTORY TABLE
      ============================== */}
      {!loading && !error && (
        <div className="inventory-table-container">

          <table className="inventory-table">

            <thead>
              <tr>
                <th>Ingredient</th>
                <th>Quantity</th>
                <th>Unit</th>
                <th>Minimum Stock</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>

            <tbody>

              {inventory.map((item) => {

                const isLowStock =
                  item.quantity <= item.minimum_stock;

                return (
                  <tr key={item._id}>

                    <td>
                      <div className="ingredient-name">
                        🥕 {item.ingredient_name}
                      </div>
                    </td>

                    <td>
                      <strong>
                        {item.quantity}
                      </strong>
                    </td>

                    <td>
                      {item.unit}
                    </td>

                    <td>
                      {item.minimum_stock}
                    </td>

                    <td>

                      {isLowStock ? (
                        <span className="status low">
                          ⚠ Low Stock
                        </span>
                      ) : (
                        <span className="status healthy">
                          ✓ Healthy
                        </span>
                      )}

                    </td>

                    <td>

                      <div className="action-buttons">

                        <button
                          className="edit-btn"
                          onClick={() =>
                            handleEditClick(item)
                          }
                        >
                          ✏ Edit
                        </button>

                        <button
                          className="delete-btn"
                          onClick={() =>
                            handleDeleteInventory(item)
                          }
                        >
                          🗑 Delete
                        </button>

                      </div>

                    </td>

                  </tr>
                );

              })}

            </tbody>

          </table>

        </div>
      )}

    </main>
  );
}

export default Inventory;