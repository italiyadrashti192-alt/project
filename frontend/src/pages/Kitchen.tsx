import { useEffect, useState } from "react";
import "./Kitchen.css";

interface KitchenIngredient {
  ingredient_name: string;
  quantity_required: number;
  unit: string;
}

interface KitchenOrder {
  _id: string;
  order_id: string;
  food_name: string;
  quantity: number;
  status: string;
  estimated_time: number;
  ingredients: KitchenIngredient[];
}

interface KitchenResponse {
  status: string;
  count: number;
  kitchen_orders: KitchenOrder[];
}

function Kitchen() {
  const [orders, setOrders] = useState<KitchenOrder[]>([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");

  const fetchKitchenOrders = () => {
    fetch("http://127.0.0.1:8000/kitchen/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch kitchen orders");
        }
        return response.json();
      })
      .then((data: KitchenResponse) => {
        setOrders(data.kitchen_orders);
      })
      .catch((error) => {
        console.error("Kitchen API Error:", error);
        setMessage("Failed to load kitchen orders");
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchKitchenOrders();
  }, []);

  const startOrder = async (id: string) => {
    try {
      setMessage("");

      const response = await fetch(
        `http://127.0.0.1:8000/kitchen/${id}/start`,
        {
          method: "POST",
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.detail || "Unable to start order");
        return;
      }

      setMessage("Order started successfully");
      fetchKitchenOrders();
    } catch (error) {
      console.error(error);
      setMessage("Something went wrong");
    }
  };

  const markReady = async (id: string) => {
    try {
      setMessage("");

      const response = await fetch(
        `http://127.0.0.1:8000/kitchen/${id}/ready`,
        {
          method: "POST",
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.detail || "Unable to mark order as ready");
        return;
      }

      setMessage("Order marked as ready");
      fetchKitchenOrders();
    } catch (error) {
      console.error(error);
      setMessage("Something went wrong");
    }
  };

  if (loading) {
    return (
      <main className="kitchen-page">
        <h1>Kitchen</h1>
        <p>Loading kitchen orders...</p>
      </main>
    );
  }

  return (
    <main className="kitchen-page">
      <div className="kitchen-header">
        <div>
          <p className="page-label">Kitchen Management</p>
          <h1>Kitchen Orders 👨‍🍳</h1>
          <p>
            Manage incoming orders, prepare food and update order status.
          </p>
        </div>

        <button
          className="refresh-btn"
          onClick={fetchKitchenOrders}
        >
          🔄 Refresh
        </button>
      </div>

      {message && (
        <div className="kitchen-message">
          {message}
        </div>
      )}

      {orders.length === 0 ? (
        <div className="empty-kitchen">
          <div>🍽️</div>
          <h2>No Kitchen Orders</h2>
          <p>There are currently no orders in the kitchen.</p>
        </div>
      ) : (
        <div className="kitchen-grid">
          {orders.map((order) => (
            <div className="kitchen-card" key={order._id}>
              
              <div className="kitchen-card-top">
                <div>
                  <span className="order-label">Order ID</span>
                  <h3>{order.order_id}</h3>
                </div>

                <span
                  className={`status-badge ${order.status.toLowerCase()}`}
                >
                  {order.status}
                </span>
              </div>

              <div className="food-section">
                <span className="food-icon">🍕</span>

                <div>
                  <span className="food-label">Food</span>
                  <h2>{order.food_name}</h2>
                </div>
              </div>

              <div className="order-details">
                <div>
                  <span>Quantity</span>
                  <strong>{order.quantity}</strong>
                </div>

                <div>
                  <span>Estimated Time</span>
                  <strong>{order.estimated_time} min</strong>
                </div>
              </div>

              <div className="ingredients-section">
                <h4>Required Ingredients</h4>

                {order.ingredients.map((ingredient, index) => (
                  <div
                    className="ingredient-row"
                    key={index}
                  >
                    <span>{ingredient.ingredient_name}</span>

                    <strong>
                      {ingredient.quantity_required}{" "}
                      {ingredient.unit}
                    </strong>
                  </div>
                ))}
              </div>

              <div className="kitchen-actions">
                {order.status.toLowerCase() === "pending" && (
                  <button
                    className="start-btn"
                    onClick={() => startOrder(order._id)}
                  >
                    ▶ Start Order
                  </button>
                )}

                {order.status.toLowerCase() === "preparing" && (
                  <button
                    className="ready-btn"
                    onClick={() => markReady(order._id)}
                  >
                    ✅ Mark Ready
                  </button>
                )}

                {order.status.toLowerCase() === "ready" && (
                  <div className="ready-text">
                    ✅ Food is Ready
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}

export default Kitchen;