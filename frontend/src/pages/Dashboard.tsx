// import "./Dashboard.css";

// function Dashboard() {
//   return (
//     <div className="dashboard">

//       <div className="welcome">
//         <p>Welcome back 👋</p>

//         <h1>Admin Dashboard</h1>

//         <span>
//           Overview of your AI Food Management System
//         </span>
//       </div>

//       <div className="dashboard-cards">

//         <div className="dashboard-card">
//           <div className="card-icon orange">
//             🛍
//           </div>

//           <p>Total Orders</p>
//           <h2>7</h2>
//         </div>

//         <div className="dashboard-card">
//           <div className="card-icon yellow">
//             🕐
//           </div>

//           <p>Placed Orders</p>
//           <h2>4</h2>
//         </div>

//         <div className="dashboard-card">
//           <div className="card-icon green">
//             ✓
//           </div>

//           <p>Completed Orders</p>
//           <h2>1</h2>
//         </div>

//         <div className="dashboard-card">
//           <div className="card-icon red">
//             ×
//           </div>

//           <p>Cancelled Orders</p>
//           <h2>1</h2>
//         </div>

//       </div>

//     </div>
//   );
// }

// export default Dashboard;


// import "./Dashboard.css";

// function Dashboard() {
//   return (
//     <main className="dashboard">

//       <div className="welcome">
//         <p>Welcome back 👋</p>

//         <h1>Admin Dashboard</h1>

//         <span>
//           Overview of your AI Food Management System
//         </span>
//       </div>


//       <div className="dashboard-cards">

//         <div className="dashboard-card">
//           <div className="card-icon">📦</div>
//           <p>Total Orders</p>
//           <h2>0</h2>
//         </div>


//         <div className="dashboard-card">
//           <div className="card-icon">⏰</div>
//           <p>Pending Orders</p>
//           <h2>0</h2>
//         </div>


//         <div className="dashboard-card">
//           <div className="card-icon">👨‍🍳</div>
//           <p>Kitchen Orders</p>
//           <h2>0</h2>
//         </div>


//         <div className="dashboard-card">
//           <div className="card-icon">⚠️</div>
//           <p>Low Stock Items</p>
//           <h2>0</h2>
//         </div>

//       </div>

//     </main>
//   );
// }

// export default Dashboard;

// import { useEffect, useState } from "react";
// import "./Dashboard.css";

// interface InventoryItem {
//   _id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   minimum_stock: number;
// }

// interface InventoryResponse {
//   status: string;
//   count: number;
//   inventory: InventoryItem[];
// }

// function Dashboard() {

//   const [inventoryCount, setInventoryCount] = useState(0);
//   const [lowStockCount, setLowStockCount] = useState(0);

//   useEffect(() => {

//     fetch("http://127.0.0.1:8000/inventory/")
//       .then((response) => {

//         if (!response.ok) {
//           throw new Error("Failed to fetch inventory");
//         }

//         return response.json();
//       })

//       .then((data: InventoryResponse) => {

//         setInventoryCount(data.count);

//         const lowStock = data.inventory.filter(
//           (item) =>
//             item.quantity <= item.minimum_stock
//         );

//         setLowStockCount(lowStock.length);

//       })

//       .catch((error) => {

//         console.error(
//           "Inventory API Error:",
//           error
//         );

//       });

//   }, []);


//   return (
//     <main className="dashboard">

//       <div className="welcome">

//         <p>Welcome back 👋</p>

//         <h1>
//           Admin Dashboard
//         </h1>

//         <span>
//           Overview of your AI Food Management System
//         </span>

//       </div>


//       <div className="dashboard-cards">

//         {/* TOTAL ORDERS */}

//         <div className="dashboard-card">

//           <div className="card-icon">
//             📦
//           </div>

//           <p>
//             Total Orders
//           </p>

//           <h2>
//             0
//           </h2>

//         </div>


//         {/* PENDING ORDERS */}

//         <div className="dashboard-card">

//           <div className="card-icon">
//             ⏰
//           </div>

//           <p>
//             Pending Orders
//           </p>

//           <h2>
//             0
//           </h2>

//         </div>


//         {/* INVENTORY */}

//         <div className="dashboard-card">

//           <div className="card-icon">
//             🥕
//           </div>

//           <p>
//             Inventory Items
//           </p>

//           <h2>
//             {inventoryCount}
//           </h2>

//         </div>


//         {/* LOW STOCK */}

//         <div className="dashboard-card">

//           <div className="card-icon">
//             ⚠️
//           </div>

//           <p>
//             Low Stock Items
//           </p>

//           <h2>
//             {lowStockCount}
//           </h2>

//         </div>

//       </div>

//     </main>
//   );
// }

// export default Dashboard;


// import { useEffect, useState } from "react";
// import "./Dashboard.css";

// interface InventoryItem {
//   _id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   minimum_stock: number;
// }

// interface InventoryResponse {
//   status: string;
//   count: number;
//   inventory: InventoryItem[];
// }

// interface SupplierResponse {
//   status: string;
//   count: number;
//   suppliers: Supplier[];
// }


// interface Supplier {
//   _id: string;
//   name: string;
//   contact_person: string;
//   phone: string;
//   email: string;
//   address: string;
// }
// interface PurchaseOrderResponse {
//   status: string;
//   count: number;
//   purchase_orders: PurchaseOrder[];
// }

// interface PurchaseOrder {
//   _id: string;
//   supplier_id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   status: string;
// }

// function Dashboard() {
//   const [inventoryCount, setInventoryCount] = useState(0);
//   const [lowStockCount, setLowStockCount] = useState(0);
//   const [supplierCount, setSupplierCount] = useState(0);
//   const [purchaseOrderCount, setPurchaseOrderCount] = useState(0);
//   useEffect(() => {
//     // =========================
//     // GET INVENTORY
//     // =========================
//     fetch("http://127.0.0.1:8000/inventory/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch inventory");
//         }

//         return response.json();
//       })
//       .then((data: InventoryResponse) => {
//         setInventoryCount(data.count);

//         const lowStock = data.inventory.filter(
//           (item) => item.quantity <= item.minimum_stock
//         );

//         setLowStockCount(lowStock.length);
//       })
//       .catch((error) => {
//         console.error("Inventory API Error:", error);
//       });

//     // =========================
//     // GET SUPPLIERS
//     // =========================
//     fetch("http://127.0.0.1:8000/suppliers/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch suppliers");
//         }

//         return response.json();
//       })
//       .then((data: SupplierResponse) => {
//         setSupplierCount(data.count);
//       })
//       .catch((error) => {
//         console.error("Supplier API Error:", error);
//       });
//   }, []);

//   return (
//     <main className="dashboard">

//       {/* =========================
//           WELCOME
//       ========================= */}
//       <div className="welcome">
//         <p>Welcome back 👋</p>

//         <h1>Kitchen & Inventory Dashboard</h1>

//         <span>
//           Manage inventory, suppliers, purchase orders and kitchen operations
//         </span>
//       </div>

//       {/* =========================
//           DASHBOARD CARDS
//       ========================= */}
//       <div className="dashboard-cards">

//         {/* INVENTORY */}
//         <div className="dashboard-card">
//           <div className="card-icon">📦</div>

//           <p>Inventory Items</p>

//           <h2>{inventoryCount}</h2>
//         </div>

//         {/* LOW STOCK */}
//         <div className="dashboard-card">
//           <div className="card-icon">⚠️</div>

//           <p>Low Stock Items</p>

//           <h2>{lowStockCount}</h2>
//         </div>

//         {/* SUPPLIERS */}
//         <div className="dashboard-card">
//           <div className="card-icon">🏭</div>

//           <p>Suppliers</p>

//           <h2>{supplierCount}</h2>
//         </div>

//         {/* KITCHEN ORDERS - FUTURE */}
//         <div className="dashboard-card">
//           <div className="card-icon">👨‍🍳</div>

//           <p>Kitchen Orders</p>

//           <h2>0</h2>
//         </div>

//         {/* PURCHASE ORDERS - FUTURE */}
//         <div className="dashboard-card">
//           <div className="card-icon">📋</div>

//           <p>Purchase Orders</p>

//           <h2>0</h2>
//         </div>

//       </div>

//     </main>
//   );
// }

// export default Dashboard;



// import { useEffect, useState } from "react";
// import "./Dashboard.css";

// interface InventoryItem {
//   _id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   minimum_stock: number;
// }

// interface InventoryResponse {
//   status: string;
//   count: number;
//   inventory: InventoryItem[];
// }

// interface Supplier {
//   _id: string;
//   name: string;
//   contact_person: string;
//   phone: string;
//   email: string;
//   address: string;
// }

// interface SupplierResponse {
//   status: string;
//   count: number;
//   suppliers: Supplier[];
// }

// interface PurchaseOrder {
//   _id: string;
//   supplier_id: string;
//   ingredient_name: string;
//   quantity: number;
//   unit: string;
//   status: string;
// }

// interface PurchaseOrderResponse {
//   status: string;
//   count: number;
//   purchase_orders: PurchaseOrder[];
// }

// function Dashboard() {
//   const [inventoryCount, setInventoryCount] = useState(0);
//   const [lowStockCount, setLowStockCount] = useState(0);
//   const [supplierCount, setSupplierCount] = useState(0);
//   const [purchaseOrderCount, setPurchaseOrderCount] = useState(0);

//   useEffect(() => {
//     // =========================
//     // GET INVENTORY
//     // =========================
//     fetch("http://127.0.0.1:8000/inventory/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch inventory");
//         }

//         return response.json();
//       })
//       .then((data: InventoryResponse) => {
//         setInventoryCount(data.count);

//         const lowStock = data.inventory.filter(
//           (item) => item.quantity <= item.minimum_stock
//         );

//         setLowStockCount(lowStock.length);
//       })
//       .catch((error) => {
//         console.error("Inventory API Error:", error);
//       });

//     // =========================
//     // GET SUPPLIERS
//     // =========================
//     fetch("http://127.0.0.1:8000/suppliers/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch suppliers");
//         }

//         return response.json();
//       })
//       .then((data: SupplierResponse) => {
//         setSupplierCount(data.count);
//       })
//       .catch((error) => {
//         console.error("Supplier API Error:", error);
//       });

//     // =========================
//     // GET PURCHASE ORDERS
//     // =========================
//     fetch("http://127.0.0.1:8000/purchase-orders/")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch purchase orders");
//         }

//         return response.json();
//       })
//       .then((data: PurchaseOrderResponse) => {
//         setPurchaseOrderCount(data.count);
//       })
//       .catch((error) => {
//         console.error("Purchase Order API Error:", error);
//       });
//   }, []);

//   return (
//     <main className="dashboard">

//       {/* =========================
//           WELCOME
//       ========================= */}
//       <div className="welcome">
//         <p>Welcome back 👋</p>

//         <h1>Kitchen & Inventory Dashboard</h1>

//         <span>
//           Manage inventory, suppliers, purchase orders and kitchen operations
//         </span>
//       </div>

//       {/* =========================
//           DASHBOARD CARDS
//       ========================= */}
//       <div className="dashboard-cards">

//         {/* INVENTORY */}
//         <div className="dashboard-card">
//           <div className="card-icon">📦</div>

//           <p>Inventory Items</p>

//           <h2>{inventoryCount}</h2>
//         </div>

//         {/* LOW STOCK */}
//         <div className="dashboard-card">
//           <div className="card-icon">⚠️</div>

//           <p>Low Stock Items</p>

//           <h2>{lowStockCount}</h2>
//         </div>

//         {/* SUPPLIERS */}
//         <div className="dashboard-card">
//           <div className="card-icon">🏭</div>

//           <p>Suppliers</p>

//           <h2>{supplierCount}</h2>
//         </div>

//         {/* KITCHEN ORDERS */}
//         <div className="dashboard-card">
//           <div className="card-icon">👨‍🍳</div>

//           <p>Kitchen Orders</p>

//           <h2>0</h2>
//         </div>

//         {/* PURCHASE ORDERS */}
//         <div className="dashboard-card">
//           <div className="card-icon">📋</div>

//           <p>Purchase Orders</p>

//           <h2>{purchaseOrderCount}</h2>
//         </div>

//       </div>

//     </main>
//   );
// }

// export default Dashboard;



import { useCallback, useEffect, useState } from "react";
import "./Dashboard.css";

interface InventoryItem {
  _id: string;
  ingredient_name: string;
  quantity: number;
  unit: string;
  minimum_stock: number;
}

interface InventoryResponse {
  status: string;
  count: number;
  inventory: InventoryItem[];
}

interface SupplierResponse {
  status: string;
  count: number;
  suppliers: unknown[];
}

interface PurchaseOrderResponse {
  status: string;
  count: number;
  purchase_orders: unknown[];
}

interface KitchenResponse {
  status: string;
  count: number;
  kitchen_orders: unknown[];
}

function Dashboard() {
  const [inventoryCount, setInventoryCount] = useState(0);
  const [lowStockCount, setLowStockCount] = useState(0);
  const [supplierCount, setSupplierCount] = useState(0);
  const [purchaseOrderCount, setPurchaseOrderCount] = useState(0);
  const [kitchenOrderCount, setKitchenOrderCount] = useState(0);

  const fetchDashboardData = useCallback(async () => {
    try {
      // INVENTORY
      const inventoryResponse = await fetch(
        "http://127.0.0.1:8000/inventory/"
      );

      if (!inventoryResponse.ok) {
        throw new Error("Failed to fetch inventory");
      }

      const inventoryData: InventoryResponse =
        await inventoryResponse.json();

      setInventoryCount(inventoryData.count);

      const lowStock = inventoryData.inventory.filter(
        (item) => item.quantity <= item.minimum_stock
      );

      setLowStockCount(lowStock.length);

      // SUPPLIERS
      const supplierResponse = await fetch(
        "http://127.0.0.1:8000/suppliers/"
      );

      if (!supplierResponse.ok) {
        throw new Error("Failed to fetch suppliers");
      }

      const supplierData: SupplierResponse =
        await supplierResponse.json();

      setSupplierCount(supplierData.count);

      // PURCHASE ORDERS
      const purchaseOrderResponse = await fetch(
        "http://127.0.0.1:8000/purchase-orders/"
      );

      if (!purchaseOrderResponse.ok) {
        throw new Error("Failed to fetch purchase orders");
      }

      const purchaseOrderData: PurchaseOrderResponse =
        await purchaseOrderResponse.json();

      setPurchaseOrderCount(purchaseOrderData.count);

      // KITCHEN ORDERS
      const kitchenResponse = await fetch(
        "http://127.0.0.1:8000/kitchen/"
      );

      if (!kitchenResponse.ok) {
        throw new Error("Failed to fetch kitchen orders");
      }

      const kitchenData: KitchenResponse =
        await kitchenResponse.json();

      setKitchenOrderCount(kitchenData.count);

    } catch (error) {
      console.error("Dashboard API Error:", error);
    }
  }, []);

  useEffect(() => {
    // Fetch immediately when dashboard opens
    fetchDashboardData();

    // Automatically refresh every 5 seconds
    const interval = setInterval(() => {
      fetchDashboardData();
    }, 5000);

    // Stop refresh when leaving dashboard
    return () => {
      clearInterval(interval);
    };
  }, [fetchDashboardData]);

  return (
    <main className="dashboard">
      <div className="welcome">
        <p>Welcome back 👋</p>

        <h1>Kitchen & Inventory Dashboard</h1>

        <span>
          Manage inventory, suppliers, purchase orders and kitchen operations
        </span>
      </div>

      <div className="dashboard-cards">

        {/* INVENTORY */}
        <div className="dashboard-card">
          <div className="card-icon">📦</div>
          <p>Inventory Items</p>
          <h2>{inventoryCount}</h2>
        </div>

        {/* LOW STOCK */}
        <div className="dashboard-card">
          <div className="card-icon">⚠️</div>
          <p>Low Stock Items</p>
          <h2>{lowStockCount}</h2>
        </div>

        {/* SUPPLIERS */}
        <div className="dashboard-card">
          <div className="card-icon">🏭</div>
          <p>Suppliers</p>
          <h2>{supplierCount}</h2>
        </div>

        {/* KITCHEN ORDERS */}
        <div className="dashboard-card">
          <div className="card-icon">👨‍🍳</div>
          <p>Kitchen Orders</p>
          <h2>{kitchenOrderCount}</h2>
        </div>

        {/* PURCHASE ORDERS */}
        <div className="dashboard-card">
          <div className="card-icon">📋</div>
          <p>Purchase Orders</p>
          <h2>{purchaseOrderCount}</h2>
        </div>

      </div>
    </main>
  );
}

export default Dashboard;