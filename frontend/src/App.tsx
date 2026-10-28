// import { useState } from 'react'
// import heroImg from './assets/hero.png'
// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <section id="center">
//         <div className="hero">
//           <img src={heroImg} className="base" width="170" height="179" alt="" />
//           <img src={reactLogo} className="framework" alt="React logo" />
//           <img src={viteLogo} className="vite" alt="Vite logo" />
//         </div>
//         <div>
//           <h1>Get started</h1>
//           <p>
//             Edit <code>src/App.tsx</code> and save to test <code>HMR</code>
//           </p>
//         </div>
//         <button
//           type="button"
//           className="counter"
//           onClick={() => setCount((count) => count + 1)}
//         >
//           Count is {count}
//         </button>
//       </section>

//       <div className="ticks"></div>

//       <section id="next-steps">
//         <div id="docs">
//           <svg className="icon" role="presentation" aria-hidden="true">
//             <use href="/icons.svg#documentation-icon"></use>
//           </svg>
//           <h2>Documentation</h2>
//           <p>Your questions, answered</p>
//           <ul>
//             <li>
//               <a href="https://vite.dev/" target="_blank">
//                 <img className="logo" src={viteLogo} alt="" />
//                 Explore Vite
//               </a>
//             </li>
//             <li>
//               <a href="https://react.dev/" target="_blank">
//                 <img className="button-icon" src={reactLogo} alt="" />
//                 Learn more
//               </a>
//             </li>
//           </ul>
//         </div>
//         <div id="social">
//           <svg className="icon" role="presentation" aria-hidden="true">
//             <use href="/icons.svg#social-icon"></use>
//           </svg>
//           <h2>Connect with us</h2>
//           <p>Join the Vite community</p>
//           <ul>
//             <li>
//               <a href="https://github.com/vitejs/vite" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#github-icon"></use>
//                 </svg>
//                 GitHub
//               </a>
//             </li>
//             <li>
//               <a href="https://chat.vite.dev/" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#discord-icon"></use>
//                 </svg>
//                 Discord
//               </a>
//             </li>
//             <li>
//               <a href="https://x.com/vite_js" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#x-icon"></use>
//                 </svg>
//                 X.com
//               </a>
//             </li>
//             <li>
//               <a href="https://bsky.app/profile/vite.dev" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#bluesky-icon"></use>
//                 </svg>
//                 Bluesky
//               </a>
//             </li>
//           </ul>
//         </div>
//       </section>

//       <div className="ticks"></div>
//       <section id="spacer"></section>
//     </>
//   )
// }

// export default App



// import './App.css'

// function App() {
//   return (
//     <div className="app">

//       {/* SIDEBAR */}
//       <aside className="sidebar">

//         <div className="logo">
//           🍴
//           <span>AI Food</span>
//         </div>

//         <p className="menu-title">MAIN MENU</p>

//         <nav>
//           <button className="nav-item active">
//             🏠 <span>Dashboard</span>
//           </button>

//           <button className="nav-item">
//             🍳 <span>Kitchen</span>
//           </button>

//           <button className="nav-item">
//             📦 <span>Inventory</span>
//           </button>

//           <button className="nav-item">
//             🚚 <span>Suppliers</span>
//           </button>

//           <button className="nav-item">
//             🛒 <span>Purchase Orders</span>
//           </button>

//           <button className="nav-item">
//             🤖 <span>AI Analysis</span>
//           </button>
//         </nav>

//       </aside>


//       {/* MAIN CONTENT */}
//       <main className="main-content">

//         {/* HEADER */}
//         <header className="topbar">

//           <div>
//             <h1>AI Food Management</h1>
//             <p>Kitchen & Inventory Management System</p>
//           </div>

//           <div className="profile">
//             👤
//             <span>Member 3</span>
//           </div>

//         </header>


//         {/* DASHBOARD */}
//         <section className="dashboard">

//           <h2>Dashboard</h2>

//           <p className="welcome">
//             Welcome to your Kitchen & Inventory Management Dashboard 👋
//           </p>


//           {/* STAT CARDS */}
//           <div className="stats">

//             <div className="stat-card">
//               <div className="stat-icon">🍳</div>
//               <div>
//                 <h3>Kitchen Orders</h3>
//                 <p>Manage incoming food orders</p>
//               </div>
//             </div>


//             <div className="stat-card">
//               <div className="stat-icon">📦</div>
//               <div>
//                 <h3>Inventory</h3>
//                 <p>Monitor ingredient stock</p>
//               </div>
//             </div>


//             <div className="stat-card">
//               <div className="stat-icon">🚚</div>
//               <div>
//                 <h3>Suppliers</h3>
//                 <p>Manage suppliers</p>
//               </div>
//             </div>


//             <div className="stat-card">
//               <div className="stat-icon">🤖</div>
//               <div>
//                 <h3>AI Analysis</h3>
//                 <p>Predict future demand</p>
//               </div>
//             </div>

//           </div>


//           {/* FLOW */}
//           <section className="flow-section">

//             <h2>Management Flow</h2>

//             <div className="flow">

//               <div className="flow-box">
//                 🍳
//                 <strong>Kitchen</strong>
//                 <span>Incoming Orders</span>
//               </div>

//               <div className="arrow">→</div>

//               <div className="flow-box">
//                 📦
//                 <strong>Inventory</strong>
//                 <span>Check Stock</span>
//               </div>

//               <div className="arrow">→</div>

//               <div className="flow-box">
//                 🚚
//                 <strong>Supplier</strong>
//                 <span>Restock</span>
//               </div>

//               <div className="arrow">→</div>

//               <div className="flow-box">
//                 🤖
//                 <strong>AI Analysis</strong>
//                 <span>Demand Prediction</span>
//               </div>

//             </div>

//           </section>


//           {/* BACKEND STATUS */}
//           <section className="connection-section">

//             <h2>Backend Connection</h2>

//             <div className="connection-card">

//               <div className="status-dot"></div>

//               <div>
//                 <strong>FastAPI Backend</strong>
//                 <p>Ready to connect</p>
//               </div>

//               <span className="status-text">
//                 Backend API
//               </span>

//             </div>

//           </section>

//         </section>

//       </main>

//     </div>
//   )
// }

// export default App

// import "./App.css";

// function App() {
//   return (
//     <div className="app">
//       <h1>AI Food Management</h1>
//       <p>Kitchen & Inventory Management System</p>
//     </div>
//   );
// }

// export default App;


// import "./App.css";

// function App() {
//   return (
//     <div className="dashboard">

//       {/* ================= SIDEBAR ================= */}
//       <aside className="sidebar">

//         {/* Logo / Brand */}
//         <div className="brand">
//           <div className="brand-icon">🍴</div>

//           <div>
//             <h2>AI Food</h2>
//             <p>Management</p>
//           </div>
//         </div>

//         {/* Menu Title */}
//         <div className="menu-title">
//           MAIN MENU
//         </div>

//         {/* Navigation */}
//         <nav className="sidebar-menu">

//           <div className="menu-item active">
//             <span className="menu-icon">▦</span>
//             <span>Dashboard</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">🛍</span>
//             <span>Orders</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">🏪</span>
//             <span>Restaurants</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">👨‍🍳</span>
//             <span>Kitchen</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">🚚</span>
//             <span>Deliveries</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">📦</span>
//             <span>Inventory</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">🥕</span>
//             <span>Ingredients</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">🚚</span>
//             <span>Suppliers</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">📋</span>
//             <span>Purchase Orders</span>
//           </div>

//           <div className="menu-item">
//             <span className="menu-icon">🤖</span>
//             <span>AI Analysis</span>
//           </div>

//         </nav>

//       </aside>


//       {/* ================= MAIN CONTENT ================= */}
//       <main className="main-content">

//         {/* Top Header */}
//         <header className="top-header">

//           <div className="header-brand">

//             <div className="header-icon">
//               🍴
//             </div>

//             <div>
//               <h2>AI Food Management</h2>
//               <p>Smart Restaurant Management</p>
//             </div>

//           </div>

//           <button className="notification">
//             🔔
//           </button>

//         </header>


//         {/* Dashboard Content */}
//         <section className="content">

//           <div className="welcome">
//             Welcome back 👋
//           </div>

//           <h1>Admin Dashboard</h1>

//           <p className="subtitle">
//             Overview of your AI Food Management System
//           </p>


//           {/* Dashboard Cards */}
//           <div className="dashboard-cards">

//             <div className="dashboard-card">
//               <div className="card-icon">🛍</div>

//               <p>Total Orders</p>

//               <h2>7</h2>
//             </div>


//             <div className="dashboard-card">
//               <div className="card-icon">⏰</div>

//               <p>Placed Orders</p>

//               <h2>4</h2>
//             </div>


//             <div className="dashboard-card">
//               <div className="card-icon">✓</div>

//               <p>Completed Orders</p>

//               <h2>1</h2>
//             </div>


//             <div className="dashboard-card">
//               <div className="card-icon">✕</div>

//               <p>Cancelled Orders</p>

//               <h2>1</h2>
//             </div>

//           </div>


//           {/* Member 3 Cards */}
//           <div className="dashboard-cards member-cards">

//             <div className="dashboard-card">
//               <div className="card-icon">📦</div>

//               <p>Inventory Items</p>

//               <h2>4</h2>
//             </div>


//             <div className="dashboard-card">
//               <div className="card-icon">👨‍🍳</div>

//               <p>Kitchen Orders</p>

//               <h2>1</h2>
//             </div>


//             <div className="dashboard-card">
//               <div className="card-icon">🚚</div>

//               <p>Suppliers</p>

//               <h2>1</h2>
//             </div>


//             <div className="dashboard-card">
//               <div className="card-icon">⚠</div>

//               <p>Low Stock Items</p>

//               <h2>0</h2>
//             </div>

//           </div>

//         </section>

//       </main>

//     </div>
//   );
// }

// export default App;


// import Sidebar from "./components/Sidebar";
// import Header from "./components/Header";
// import Dashboard from "./pages/Dashboard";
// import "./App.css";

// function App() {
//   return (
//     <div className="app">

//       <Sidebar />

//       <main className="main-content">

//         <Header />

//         <Dashboard />

//       </main>

//     </div>
//   );
// }

// export default App;


// import "./App.css"

// function App() {
//   return (
//     <div className="app">

//       {/* SIDEBAR */}
//       <aside className="sidebar">

//         <div className="brand">
//           <div className="brand-icon">🍴</div>

//           <div>
//             <h2>AI Food</h2>
//             <p>Management</p>
//           </div>
//         </div>

//         <div className="menu-title">
//           MAIN MENU
//         </div>

//         <nav className="sidebar-menu">

//           <button className="menu-item active">
//             <span>▦</span>
//             Dashboard
//           </button>

//           <button className="menu-item">
//             <span>▣</span>
//             Orders
//           </button>

//           <button className="menu-item">
//             <span>⌂</span>
//             Restaurants
//           </button>

//           <button className="menu-item">
//             <span>♨</span>
//             Kitchen
//           </button>

//           <button className="menu-item">
//             <span>🚚</span>
//             Deliveries
//           </button>

//           <button className="menu-item">
//             <span>□</span>
//             Inventory
//           </button>

//           <button className="menu-item">
//             <span>🥕</span>
//             Ingredients
//           </button>

//           <button className="menu-item">
//             <span>♙</span>
//             Suppliers
//           </button>

//           <button className="menu-item">
//             <span>▤</span>
//             Purchase Orders
//           </button>

//           <button className="menu-item">
//             <span>✦</span>
//             AI Analysis
//           </button>

//         </nav>

//       </aside>


//       {/* MAIN CONTENT */}
//       <main className="main-content">

//         {/* HEADER */}
//         <header className="top-header">

//           <div className="header-brand">

//             <div className="header-icon">
//               🍴
//             </div>

//             <div>
//               <h2>AI Food Management</h2>
//               <p>Smart Restaurant Management</p>
//             </div>

//           </div>

//           <button className="notification">
//             🔔
//           </button>

//         </header>


//         {/* DASHBOARD */}
//         <section className="dashboard">

//           <p className="welcome">
//             Welcome back 👋
//           </p>

//           <h1>
//             Admin Dashboard
//           </h1>

//           <p className="subtitle">
//             Overview of your AI Food Management System
//           </p>


//           {/* STAT CARDS */}
//           <div className="stats-grid">

//             <div className="stat-card">

//               <div className="stat-icon orange">
//                 🛒
//               </div>

//               <p>Total Orders</p>

//               <h2>7</h2>

//             </div>


//             <div className="stat-card">

//               <div className="stat-icon yellow">
//                 🕒
//               </div>

//               <p>Placed Orders</p>

//               <h2>4</h2>

//             </div>


//             <div className="stat-card">

//               <div className="stat-icon green">
//                 ✓
//               </div>

//               <p>Completed Orders</p>

//               <h2>1</h2>

//             </div>


//             <div className="stat-card">

//               <div className="stat-icon red">
//                 ✕
//               </div>

//               <p>Cancelled Orders</p>

//               <h2>1</h2>

//             </div>

//           </div>


//           {/* MODULE CARDS */}
//           <div className="module-grid">

//             <div className="module-card">
//               <h3>Kitchen Management</h3>
//               <p>
//                 Manage incoming kitchen orders,
//                 ingredients and preparation status.
//               </p>

//               <button>
//                 Open Kitchen
//               </button>
//             </div>


//             <div className="module-card">
//               <h3>Inventory Management</h3>
//               <p>
//                 Monitor stock levels and
//                 identify low-stock ingredients.
//               </p>

//               <button>
//                 View Inventory
//               </button>
//             </div>


//             <div className="module-card">
//               <h3>Supplier Management</h3>
//               <p>
//                 Manage suppliers and
//                 purchase orders.
//               </p>

//               <button>
//                 View Suppliers
//               </button>
//             </div>


//             <div className="module-card">
//               <h3>AI Inventory Analysis</h3>
//               <p>
//                 View AI-based inventory analysis
//                 and demand predictions.
//               </p>

//               <button>
//                 View AI Analysis
//               </button>
//             </div>

//           </div>

//         </section>

//       </main>

//     </div>
//   )
// }

// export default App


// import Sidebar from "./components/Sidebar";
// import Header from "./components/Header";
// import Dashboard from "./pages/Dashboard";
// import "./App.css";

// function App() {
//   return (
//     <div className="app">

//       <Sidebar />

//       <div className="main-area">

//         <Header />

//         <Dashboard />

//       </div>

//     </div>
//   );
// }

// export default App;

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";

import Dashboard from "./pages/Dashboard";
import Inventory from "./pages/Inventory";

import Suppliers from "./pages/Suppliers";

import PurchaseOrders from "./pages/PurchaseOrders";
import Kitchen from "./pages/Kitchen";
import AIAnalysis from "./pages/AIAnalysis";

import "./App.css";

function App() {
  return (
    <BrowserRouter>

      <div className="app">

        <Sidebar />

        <div className="main-area">

          <Header />

          <Routes>

            <Route path="/" element={<Dashboard />} />

            <Route path="/inventory" element={<Inventory />} />

            <Route path="/suppliers" element={<Suppliers />} />

            <Route path="/purchase-orders" element={<PurchaseOrders />} />

            <Route path="/kitchen" element={<Kitchen />} />

             <Route
              path="/ai-analysis"
              element={<AIAnalysis />}
            />



          </Routes>

        </div>

      </div>

    </BrowserRouter>
  );
}

export default App;