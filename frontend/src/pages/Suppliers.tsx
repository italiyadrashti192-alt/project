import { useEffect, useState } from "react";
import "./Suppliers.css";

interface Supplier {
  _id: string;
  name: string;
  contact_person: string;
  phone: string;
  email: string;
  address: string;
}

interface SupplierResponse {
  status: string;
  count: number;
  suppliers: Supplier[];
}

function Suppliers() {
  const [suppliers, setSuppliers] = useState<Supplier[]>([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Add form
  const [showForm, setShowForm] = useState(false);

  const [name, setName] = useState("");
  const [contactPerson, setContactPerson] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");

  // Edit
  const [editingId, setEditingId] = useState<string | null>(null);

  // =========================
  // GET ALL SUPPLIERS
  // =========================
  const fetchSuppliers = () => {
    setLoading(true);

    fetch("http://127.0.0.1:8000/suppliers/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch suppliers");
        }

        return response.json();
      })
      .then((data: SupplierResponse) => {
        setSuppliers(data.suppliers || []);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Supplier API Error:", error);
        setError("Unable to load suppliers");
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchSuppliers();
  }, []);

  // =========================
  // CLEAR FORM
  // =========================
  const clearForm = () => {
    setName("");
    setContactPerson("");
    setPhone("");
    setEmail("");
    setAddress("");
    setEditingId(null);
    setShowForm(false);
  };

  // =========================
  // ADD SUPPLIER
  // =========================
  const handleAddSupplier = (event: React.FormEvent) => {
    event.preventDefault();

    const supplierData = {
      name,
      contact_person: contactPerson,
      phone,
      email,
      address,
    };

    fetch("http://127.0.0.1:8000/suppliers/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(supplierData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to create supplier");
        }

        return response.json();
      })
      .then(() => {
        alert("Supplier added successfully");

        clearForm();
        fetchSuppliers();
      })
      .catch((error) => {
        console.error("Add Supplier Error:", error);
        alert("Failed to add supplier");
      });
  };

  // =========================
  // EDIT SUPPLIER
  // =========================
  const handleEdit = (supplier: Supplier) => {
    setEditingId(supplier._id);

    setName(supplier.name);
    setContactPerson(supplier.contact_person);
    setPhone(supplier.phone);
    setEmail(supplier.email);
    setAddress(supplier.address);

    setShowForm(true);
  };

  // =========================
  // UPDATE SUPPLIER
  // =========================
  const handleUpdateSupplier = (event: React.FormEvent) => {
    event.preventDefault();

    if (!editingId) {
      return;
    }

    const supplierData = {
      name,
      contact_person: contactPerson,
      phone,
      email,
      address,
    };

    fetch(`http://127.0.0.1:8000/suppliers/${editingId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(supplierData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to update supplier");
        }

        return response.json();
      })
      .then(() => {
        alert("Supplier updated successfully");

        clearForm();
        fetchSuppliers();
      })
      .catch((error) => {
        console.error("Update Supplier Error:", error);
        alert("Failed to update supplier");
      });
  };

  // =========================
  // DELETE SUPPLIER
  // =========================
  const handleDelete = (supplierId: string) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this supplier?"
    );

    if (!confirmDelete) {
      return;
    }

    fetch(`http://127.0.0.1:8000/suppliers/${supplierId}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to delete supplier");
        }

        return response.json();
      })
      .then(() => {
        alert("Supplier deleted successfully");

        fetchSuppliers();
      })
      .catch((error) => {
        console.error("Delete Supplier Error:", error);
        alert("Failed to delete supplier");
      });
  };

  return (
    <main className="suppliers-page">

      {/* =========================
          HEADER
      ========================= */}
      <div className="suppliers-header">
        <div>
          <p className="suppliers-welcome">SUPPLIER MANAGEMENT</p>

          <h1>Suppliers</h1>

          <span>
            Manage your ingredient suppliers and their contact information.
          </span>
        </div>

        <button
          className="add-supplier-btn"
          onClick={() => {
            setEditingId(null);
            setShowForm(!showForm);
          }}
        >
          + Add Supplier
        </button>
      </div>

      {/* =========================
          ERROR
      ========================= */}
      {error && <div className="supplier-error">{error}</div>}

      {/* =========================
          ADD / EDIT FORM
      ========================= */}
      {showForm && (
        <div
          className={`supplier-form-container ${
            editingId ? "edit-form" : ""
          }`}
        >
          <h2>
            {editingId ? "Edit Supplier" : "Add New Supplier"}
          </h2>

          {editingId && (
            <p className="editing-supplier">
              Update supplier information below.
            </p>
          )}

          <form
            onSubmit={
              editingId
                ? handleUpdateSupplier
                : handleAddSupplier
            }
          >

            {/* NAME */}
            <div className="form-group">
              <label>Supplier Name</label>

              <input
                type="text"
                placeholder="Enter supplier name"
                value={name}
                onChange={(event) => setName(event.target.value)}
                required
              />
            </div>

            {/* CONTACT PERSON */}
            <div className="form-group">
              <label>Contact Person</label>

              <input
                type="text"
                placeholder="Enter contact person"
                value={contactPerson}
                onChange={(event) =>
                  setContactPerson(event.target.value)
                }
                required
              />
            </div>

            {/* PHONE */}
            <div className="form-group">
              <label>Phone</label>

              <input
                type="text"
                placeholder="Enter phone number"
                value={phone}
                onChange={(event) =>
                  setPhone(event.target.value)
                }
                required
              />
            </div>

            {/* EMAIL */}
            <div className="form-group">
              <label>Email</label>

              <input
                type="email"
                placeholder="Enter email address"
                value={email}
                onChange={(event) =>
                  setEmail(event.target.value)
                }
                required
              />
            </div>

            {/* ADDRESS */}
            <div className="form-group full-width">
              <label>Address</label>

              <input
                type="text"
                placeholder="Enter supplier address"
                value={address}
                onChange={(event) =>
                  setAddress(event.target.value)
                }
                required
              />
            </div>

            {/* BUTTONS */}
            <div className="form-buttons">
              <button type="submit" className="save-btn">
                {editingId ? "Update Supplier" : "Save Supplier"}
              </button>

              <button
                type="button"
                className="cancel-btn"
                onClick={clearForm}
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      {/* =========================
          SUPPLIER LIST
      ========================= */}
      <div className="supplier-table-container">

        {loading ? (
          <div className="supplier-message">
            Loading suppliers...
          </div>
        ) : suppliers.length === 0 ? (
          <div className="supplier-message">
            <h3>No Suppliers Found</h3>
            <p>Add your first supplier using the button above.</p>
          </div>
        ) : (
          <table className="supplier-table">

            <thead>
              <tr>
                <th>Supplier Name</th>
                <th>Contact Person</th>
                <th>Phone</th>
                <th>Email</th>
                <th>Address</th>
                <th>Actions</th>
              </tr>
            </thead>

            <tbody>
              {suppliers.map((supplier) => (
                <tr key={supplier._id}>

                  <td>
                    <div className="supplier-name">
                      🏭 {supplier.name}
                    </div>
                  </td>

                  <td>
                    {supplier.contact_person}
                  </td>

                  <td>
                    {supplier.phone}
                  </td>

                  <td>
                    {supplier.email}
                  </td>

                  <td>
                    {supplier.address}
                  </td>

                  <td>
                    <div className="action-buttons">

                      <button
                        className="edit-btn"
                        onClick={() => handleEdit(supplier)}
                      >
                        Edit
                      </button>

                      <button
                        className="delete-btn"
                        onClick={() =>
                          handleDelete(supplier._id)
                        }
                      >
                        Delete
                      </button>

                    </div>
                  </td>

                </tr>
              ))}
            </tbody>

          </table>
        )}

      </div>

    </main>
  );
}

export default Suppliers;