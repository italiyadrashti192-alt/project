// import "./Sidebar.css";

// function Sidebar() {
//   return (
//     <aside className="sidebar">

//       {/* Logo */}
//       <div className="sidebar-logo">
//         <div className="logo-box">
//           🍴
//         </div>

//         <div>
//           <h2>AI Food</h2>
//           <p>Management</p>
//         </div>
//       </div>

//       {/* Menu */}
//       <div className="menu-section">

//         <p className="menu-title">MAIN MENU</p>

//         <div className="menu-item active">
//           <span>▦</span>
//           <span>Dashboard</span>
//         </div>

//         <div className="menu-item">
//           <span>🛍</span>
//           <span>Orders</span>
//         </div>

//         <div className="menu-item">
//           <span>🏪</span>
//           <span>Restaurants</span>
//         </div>

//         <div className="menu-item">
//           <span>👨‍🍳</span>
//           <span>Kitchen</span>
//         </div>

//         <div className="menu-item">
//           <span>🚚</span>
//           <span>Deliveries</span>
//         </div>

//         <div className="menu-item">
//           <span>📦</span>
//           <span>Inventory</span>
//         </div>

//         <div className="menu-item">
//           <span>🥕</span>
//           <span>Ingredients</span>
//         </div>

//         <div className="menu-item">
//           <span>🚛</span>
//           <span>Suppliers</span>
//         </div>

//         <div className="menu-item">
//           <span>📋</span>
//           <span>Purchase Orders</span>
//         </div>

//         <div className="menu-item">
//           <span>🤖</span>
//           <span>AI Analysis</span>
//         </div>

//       </div>

//     </aside>
//   );
// }

// export default Sidebar;


// import "./Sidebar.css";

// function Sidebar() {
//   return (
//     <aside className="sidebar">

//       <div className="sidebar-logo">
//         <div className="logo-box">🍴</div>

//         <div>
//           <h2>AI Food</h2>
//           <p>Management</p>
//         </div>
//       </div>

//       <div className="menu-title">
//         MAIN MENU
//       </div>

//       <nav className="sidebar-menu">

//         <a href="/" className="menu-item active">
//           <span>▦</span>
//           Dashboard
//         </a>

//         <a href="/orders" className="menu-item">
//           <span>🛍</span>
//           Orders
//         </a>

//         <a href="/restaurants" className="menu-item">
//           <span>🏪</span>
//           Restaurants
//         </a>

//         <a href="/kitchen" className="menu-item">
//           <span>👨‍🍳</span>
//           Kitchen
//         </a>

//         <a href="/deliveries" className="menu-item">
//           <span>🚚</span>
//           Deliveries
//         </a>

//         <a href="/inventory" className="menu-item">
//           <span>📦</span>
//           Inventory
//         </a>

//         <a href="/ingredients" className="menu-item">
//           <span>🥕</span>
//           Ingredients
//         </a>

//         <a href="/suppliers" className="menu-item">
//           <span>🚛</span>
//           Suppliers
//         </a>

//         <a href="/purchase-orders" className="menu-item">
//           <span>📝</span>
//           Purchase Orders
//         </a>

//         <a href="/ai-analysis" className="menu-item">
//           <span>🤖</span>
//           AI Analysis
//         </a>

//       </nav>

//     </aside>
//   );
// }

// export default Sidebar;

import { NavLink } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
  return (
    <aside className="sidebar">

      <div className="sidebar-logo">
        <h2>AI Food</h2>
        <span>Management</span>
      </div>

      <nav className="sidebar-nav">

        <NavLink to="/" className="nav-item">
          <span>📊</span>
          Dashboard
        </NavLink>

        <NavLink to="/orders" className="nav-item">
          <span>🛒</span>
          Orders
        </NavLink>

        <NavLink to="/restaurants" className="nav-item">
          <span>🍽️</span>
          Restaurants
        </NavLink>

        <NavLink to="/kitchen" className="nav-item">
          <span>👨‍🍳</span>
          Kitchen
        </NavLink>

        <NavLink to="/deliveries" className="nav-item">
          <span>🚚</span>
          Deliveries
        </NavLink>

        <NavLink to="/inventory" className="nav-item">
          <span>📦</span>
          Inventory
        </NavLink>

        <NavLink to="/ingredients" className="nav-item">
          <span>🥕</span>
          Ingredients
        </NavLink>

        <NavLink to="/suppliers" className="nav-item">
          <span>🏭</span>
          Suppliers
        </NavLink>

        <NavLink to="/purchase-orders" className="nav-item">
          <span>📋</span>
          Purchase Orders
        </NavLink>

        <NavLink to="/ai-analysis" className="nav-item">
          <span>🤖</span>
          AI Analysis
        </NavLink>

      </nav>

    </aside>
  );
}

export default Sidebar;