import API_URL from "../api";
import { useEffect, useState } from "react";
import axios from "axios";

function MostReviewedProducts() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`${API_URL}/api/most_reviewed_products/`)
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching most reviewed products:", error);
      });
  }, []);

  return (
    <section className="rounded-xl bg-white p-5 shadow-sm">
      <h2 className="mb-4 text-lg font-semibold text-gray-800">
        Most Reviewed Products
      </h2>

      <div className="h-64 overflow-y-auto">
        <table className="w-full text-left">
          <thead className="sticky top-0 bg-white">
            <tr className="border-b border-gray-200 text-sm text-gray-500">
              <th className="px-3 py-2">Product</th>
              <th className="px-3 py-2">Reviews</th>
              <th className="px-3 py-2">Score</th>
            </tr>
          </thead>

          <tbody>
            {data.map((product) => (
              <tr
                key={product.product_id}
                className="border-b border-gray-100"
              >
                <td className="px-3 py-2 text-sm font-medium text-gray-800">
                  {product.product_id}
                </td>

                <td className="px-3 py-2 text-sm text-gray-600">
                  {product.review_count.toLocaleString()}
                </td>

                <td className="px-3 py-2 text-sm text-gray-600">
                  {product.avg_score}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default MostReviewedProducts;