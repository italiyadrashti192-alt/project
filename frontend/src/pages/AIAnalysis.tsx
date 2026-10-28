//     import { useEffect, useState } from "react";
// import "./AIAnalysis.css";

// interface AIAnalysisItem {
//   ingredient_name: string;
//   current_stock: number;
//   minimum_stock: number;
//   unit: string;
//   total_used: number;
//   stock_status: string;
//   demand: string;
// }

// interface AIAnalysisResponse {
//   status: string;
//   count: number;
//   analysis: AIAnalysisItem[];
// }

// function AIAnalysis() {
//   const [analysis, setAnalysis] = useState<AIAnalysisItem[]>([]);
//   const [loading, setLoading] = useState(true);
//   const [message, setMessage] = useState("");

//   const fetchAnalysis = () => {
//     setLoading(true);
//     setMessage("");

//     fetch("http://127.0.0.1:8000/ai/inventory-analysis")
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("Failed to fetch AI analysis");
//         }

//         return response.json();
//       })
//       .then((data: AIAnalysisResponse) => {
//         setAnalysis(data.analysis);
//       })
//       .catch((error) => {
//         console.error("AI Analysis API Error:", error);
//         setMessage("Failed to load AI analysis");
//       })
//       .finally(() => {
//         setLoading(false);
//       });
//   };

//   useEffect(() => {
//     fetchAnalysis();
//   }, []);

//   const getStockClass = (status: string) => {
//     if (status.toLowerCase() === "low_stock") {
//       return "low-stock";
//     }

//     return "normal-stock";
//   };

//   const getDemandClass = (demand: string) => {
//     const value = demand.toLowerCase();

//     if (value === "high") {
//       return "high-demand";
//     }

//     if (value === "medium") {
//       return "medium-demand";
//     }

//     if (value === "low") {
//       return "low-demand";
//     }

//     return "no-demand";
//   };

//   if (loading) {
//     return (
//       <main className="ai-page">
//         <div className="ai-loading">
//           <div className="ai-loading-icon">🤖</div>
//           <h2>Analyzing Inventory...</h2>
//           <p>Please wait while AI analysis is loading.</p>
//         </div>
//       </main>
//     );
//   }

//   return (
//     <main className="ai-page">

//       {/* Header */}
//       <div className="ai-header">
//         <div>
//           <p className="page-label">Artificial Intelligence</p>

//           <h1>AI Inventory Analysis 🤖</h1>

//           <p>
//             Analyze inventory stock levels, ingredient usage and demand.
//           </p>
//         </div>

//         <button className="ai-refresh-btn" onClick={fetchAnalysis}>
//           🔄 Refresh Analysis
//         </button>
//       </div>

//       {/* Error Message */}
//       {message && (
//         <div className="ai-message">
//           ⚠️ {message}
//         </div>
//       )}

//       {/* Summary Cards */}
//       <div className="ai-summary">

//         <div className="ai-summary-card">
//           <div className="summary-icon">📦</div>
//           <div>
//             <span>Total Ingredients</span>
//             <h2>{analysis.length}</h2>
//           </div>
//         </div>

//         <div className="ai-summary-card">
//           <div className="summary-icon">⚠️</div>
//           <div>
//             <span>Low Stock</span>
//             <h2>
//               {
//                 analysis.filter(
//                   (item) => item.stock_status.toLowerCase() === "low_stock"
//                 ).length
//               }
//             </h2>
//           </div>
//         </div>

//         <div className="ai-summary-card">
//           <div className="summary-icon">🔥</div>
//           <div>
//             <span>High Demand</span>
//             <h2>
//               {
//                 analysis.filter(
//                   (item) => item.demand.toLowerCase() === "high"
//                 ).length
//               }
//             </h2>
//           </div>
//         </div>

//         <div className="ai-summary-card">
//           <div className="summary-icon">📊</div>
//           <div>
//             <span>Usage Recorded</span>
//             <h2>
//               {
//                 analysis.filter(
//                   (item) => item.total_used > 0
//                 ).length
//               }
//             </h2>
//           </div>
//         </div>

//       </div>

//       {/* Analysis Table */}
//       {analysis.length === 0 ? (
//         <div className="ai-empty">
//           <div>🤖</div>
//           <h2>No Analysis Data</h2>
//           <p>
//             There is currently no inventory data available for analysis.
//           </p>
//         </div>
//       ) : (
//         <div className="ai-table-container">

//           <div className="ai-table-header">
//             <div>
//               <h2>Inventory Analysis</h2>
//               <p>AI-generated inventory insights</p>
//             </div>

//             <span className="analysis-count">
//               {analysis.length} items
//             </span>
//           </div>

//           <div className="table-wrapper">

//             <table className="ai-table">

//               <thead>
//                 <tr>
//                   <th>Ingredient</th>
//                   <th>Current Stock</th>
//                   <th>Minimum Stock</th>
//                   <th>Total Used</th>
//                   <th>Stock Status</th>
//                   <th>Demand</th>
//                 </tr>
//               </thead>

//               <tbody>

//                 {analysis.map((item, index) => (

//                   <tr key={`${item.ingredient_name}-${index}`}>

//                     <td>
//                       <div className="ingredient-name">
//                         <span className="ingredient-icon">
//                           🥕
//                         </span>

//                         <strong>
//                           {item.ingredient_name}
//                         </strong>
//                       </div>
//                     </td>

//                     <td>
//                       <strong>
//                         {item.current_stock} {item.unit}
//                       </strong>
//                     </td>

//                     <td>
//                       {item.minimum_stock} {item.unit}
//                     </td>

//                     <td>
//                       {item.total_used} {item.unit}
//                     </td>

//                     <td>
//                       <span
//                         className={`status-badge ${getStockClass(
//                           item.stock_status
//                         )}`}
//                       >
//                         {item.stock_status === "low_stock"
//                           ? "⚠️ Low Stock"
//                           : "✓ Normal"}
//                       </span>
//                     </td>

//                     <td>
//                       <span
//                         className={`demand-badge ${getDemandClass(
//                           item.demand
//                         )}`}
//                       >
//                         {item.demand === "high" && "🔥 High"}
//                         {item.demand === "medium" && "📈 Medium"}
//                         {item.demand === "low" && "📉 Low"}
//                         {item.demand === "no_usage_data" &&
//                           "➖ No Usage Data"}
//                       </span>
//                     </td>

//                   </tr>

//                 ))}

//               </tbody>

//             </table>

//           </div>

//         </div>
//       )}

//     </main>
//   );
// }

// export default AIAnalysis;


import { useEffect, useState } from "react";
import "./AIAnalysis.css";

interface AIAnalysisItem {
  ingredient_name: string;
  current_stock: number;
  minimum_stock: number;
  unit: string;
  total_used: number;
  stock_status: string;
  demand: string;
}

interface AIAnalysisResponse {
  status: string;
  count: number;
  analysis: AIAnalysisItem[];
}

function AIAnalysis() {
  const [analysis, setAnalysis] = useState<AIAnalysisItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");

  const fetchAnalysis = () => {
    setLoading(true);
    setMessage("");

    fetch("http://127.0.0.1:8000/ai/inventory-analysis")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch AI analysis");
        }

        return response.json();
      })
      .then((data: AIAnalysisResponse) => {
        setAnalysis(data.analysis);
      })
      .catch((error) => {
        console.error("AI Analysis API Error:", error);
        setMessage("Failed to load AI analysis");
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchAnalysis();
  }, []);

  // -----------------------------
  // STOCK STATUS
  // -----------------------------
  const getStockClass = (status: string) => {
    if (status.toLowerCase() === "low_stock") {
      return "low-stock";
    }

    return "normal-stock";
  };

  // -----------------------------
  // DEMAND STATUS
  // -----------------------------
  const getDemandClass = (demand: string) => {
    const value = demand.toLowerCase();

    if (value === "high") {
      return "high-demand";
    }

    if (value === "medium") {
      return "medium-demand";
    }

    if (value === "low") {
      return "low-demand";
    }

    return "no-demand";
  };

  // -----------------------------
  // AI INSIGHT DATA
  // -----------------------------

  const lowStockItems = analysis.filter(
    (item) => item.stock_status.toLowerCase() === "low_stock"
  );

  const highDemandItems = analysis.filter(
    (item) => item.demand.toLowerCase() === "high"
  );

  const mediumDemandItems = analysis.filter(
    (item) => item.demand.toLowerCase() === "medium"
  );

  const usageRecordedItems = analysis.filter(
    (item) => item.total_used > 0
  );

  const noUsageItems = analysis.filter(
    (item) => item.demand.toLowerCase() === "no_usage_data"
  );

  // -----------------------------
  // LOADING
  // -----------------------------

  if (loading) {
    return (
      <main className="ai-page">
        <div className="ai-loading">
          <div className="ai-loading-icon">🤖</div>

          <h2>Analyzing Inventory...</h2>

          <p>
            Please wait while AI analysis is loading.
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="ai-page">

      {/* =========================
          PAGE HEADER
      ========================== */}

      <div className="ai-header">

        <div>
          <p className="page-label">
            Artificial Intelligence
          </p>

          <h1>
            AI Inventory Analysis 🤖
          </h1>

          <p>
            Analyze inventory stock levels, ingredient usage and demand.
          </p>
        </div>

        <button
          className="ai-refresh-btn"
          onClick={fetchAnalysis}
        >
          🔄 Refresh Analysis
        </button>

      </div>

      {/* =========================
          ERROR MESSAGE
      ========================== */}

      {message && (
        <div className="ai-message">
          ⚠️ {message}
        </div>
      )}

      {/* =========================
          SUMMARY CARDS
      ========================== */}

      <div className="ai-summary">

        {/* TOTAL INGREDIENTS */}

        <div className="ai-summary-card">

          <div className="summary-icon">
            📦
          </div>

          <div>
            <span>Total Ingredients</span>

            <h2>
              {analysis.length}
            </h2>
          </div>

        </div>

        {/* LOW STOCK */}

        <div className="ai-summary-card">

          <div className="summary-icon">
            ⚠️
          </div>

          <div>
            <span>Low Stock</span>

            <h2>
              {lowStockItems.length}
            </h2>
          </div>

        </div>

        {/* HIGH DEMAND */}

        <div className="ai-summary-card">

          <div className="summary-icon">
            🔥
          </div>

          <div>
            <span>High Demand</span>

            <h2>
              {highDemandItems.length}
            </h2>
          </div>

        </div>

        {/* USAGE RECORDED */}

        <div className="ai-summary-card">

          <div className="summary-icon">
            📊
          </div>

          <div>
            <span>Usage Recorded</span>

            <h2>
              {usageRecordedItems.length}
            </h2>
          </div>

        </div>

      </div>

      {/* =========================
          AI INSIGHTS SECTION
      ========================== */}

      {analysis.length > 0 && (
        <div className="ai-insights-section">

          <div className="ai-insights-header">

            <div>
              <p className="page-label">
                Smart Recommendations
              </p>

              <h2>
                AI Inventory Insights 🤖
              </h2>

              <p>
                Recommendations based on current stock,
                ingredient usage and demand analysis.
              </p>
            </div>

          </div>

          <div className="ai-insights-grid">

            {/* =====================
                LOW STOCK INSIGHT
            ====================== */}

            <div className="ai-insight-card warning-insight">

              <div className="insight-icon">
                ⚠️
              </div>

              <div className="insight-content">

                <h3>
                  Low Stock Alert
                </h3>

                {lowStockItems.length > 0 ? (
                  <>
                    <p>
                      {lowStockItems.length} ingredient
                      {lowStockItems.length > 1 ? "s" : ""}{" "}
                      {lowStockItems.length > 1
                        ? "are"
                        : "is"}{" "}
                      at or below the minimum stock level.
                    </p>

                    <div className="insight-items">
                      {lowStockItems.map((item) => (
                        <span key={item.ingredient_name}>
                          {item.ingredient_name}
                        </span>
                      ))}
                    </div>
                  </>
                ) : (
                  <p>
                    All ingredients have sufficient stock.
                  </p>
                )}

              </div>

            </div>

            {/* =====================
                HIGH DEMAND INSIGHT
            ====================== */}

            <div className="ai-insight-card danger-insight">

              <div className="insight-icon">
                🔥
              </div>

              <div className="insight-content">

                <h3>
                  High Demand
                </h3>

                {highDemandItems.length > 0 ? (
                  <>
                    <p>
                      These ingredients have high usage
                      and may require additional stock.
                    </p>

                    <div className="insight-items">
                      {highDemandItems.map((item) => (
                        <span key={item.ingredient_name}>
                          {item.ingredient_name}
                        </span>
                      ))}
                    </div>
                  </>
                ) : (
                  <p>
                    No high-demand ingredients detected.
                  </p>
                )}

              </div>

            </div>

            {/* =====================
                PURCHASE RECOMMENDATION
            ====================== */}

            <div className="ai-insight-card purchase-insight">

              <div className="insight-icon">
                📦
              </div>

              <div className="insight-content">

                <h3>
                  Purchase Recommendation
                </h3>

                {lowStockItems.length > 0 ? (
                  <>
                    <p>
                      Consider creating purchase orders
                      for the following low-stock ingredients:
                    </p>

                    <div className="insight-items">

                      {lowStockItems.map((item) => (
                        <span key={item.ingredient_name}>
                          {item.ingredient_name}
                        </span>
                      ))}

                    </div>
                  </>
                ) : (
                  <p>
                    No immediate purchase recommendation.
                  </p>
                )}

              </div>

            </div>

            {/* =====================
                DEMAND INFORMATION
            ====================== */}

            <div className="ai-insight-card information-insight">

              <div className="insight-icon">
                📊
              </div>

              <div className="insight-content">

                <h3>
                  Demand Information
                </h3>

                <p>
                  {mediumDemandItems.length > 0
                    ? `${mediumDemandItems.length} ingredient${
                        mediumDemandItems.length > 1
                          ? "s have"
                          : " has"
                      } medium demand.`
                    : "No medium-demand ingredients detected."}
                </p>

                <p className="usage-text">
                  {noUsageItems.length > 0
                    ? `${noUsageItems.length} ingredient${
                        noUsageItems.length > 1
                          ? "s have"
                          : " has"
                      } no recorded usage data.`
                    : "Usage data is available for all ingredients."}
                </p>

              </div>

            </div>

          </div>

        </div>
      )}

      {/* =========================
          EMPTY STATE
      ========================== */}

      {analysis.length === 0 ? (
        <div className="ai-empty">

          <div>
            🤖
          </div>

          <h2>
            No Analysis Data
          </h2>

          <p>
            There is currently no inventory data available
            for analysis.
          </p>

        </div>
      ) : (

        /* =========================
           INVENTORY ANALYSIS TABLE
        ========================== */

        <div className="ai-table-container">

          <div className="ai-table-header">

            <div>
              <h2>
                Inventory Analysis
              </h2>

              <p>
                AI-generated inventory insights
              </p>
            </div>

            <span className="analysis-count">
              {analysis.length} items
            </span>

          </div>

          <div className="table-wrapper">

            <table className="ai-table">

              <thead>

                <tr>
                  <th>Ingredient</th>
                  <th>Current Stock</th>
                  <th>Minimum Stock</th>
                  <th>Total Used</th>
                  <th>Stock Status</th>
                  <th>Demand</th>
                </tr>

              </thead>

              <tbody>

                {analysis.map((item, index) => (

                  <tr
                    key={`${item.ingredient_name}-${index}`}
                  >

                    {/* INGREDIENT */}

                    <td>

                      <div className="ingredient-name">

                        <span className="ingredient-icon">
                          🥕
                        </span>

                        <strong>
                          {item.ingredient_name}
                        </strong>

                      </div>

                    </td>

                    {/* CURRENT STOCK */}

                    <td>

                      <strong>
                        {item.current_stock} {item.unit}
                      </strong>

                    </td>

                    {/* MINIMUM STOCK */}

                    <td>
                      {item.minimum_stock} {item.unit}
                    </td>

                    {/* TOTAL USED */}

                    <td>
                      {item.total_used} {item.unit}
                    </td>

                    {/* STOCK STATUS */}

                    <td>

                      <span
                        className={`status-badge ${getStockClass(
                          item.stock_status
                        )}`}
                      >

                        {item.stock_status === "low_stock"
                          ? "⚠️ Low Stock"
                          : "✓ Normal"}

                      </span>

                    </td>

                    {/* DEMAND */}

                    <td>

                      <span
                        className={`demand-badge ${getDemandClass(
                          item.demand
                        )}`}
                      >

                        {item.demand === "high" &&
                          "🔥 High"}

                        {item.demand === "medium" &&
                          "📈 Medium"}

                        {item.demand === "low" &&
                          "📉 Low"}

                        {item.demand === "no_usage_data" &&
                          "➖ No Usage Data"}

                      </span>

                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

      )}

    </main>
  );
}

export default AIAnalysis;