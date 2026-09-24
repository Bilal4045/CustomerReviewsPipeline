import API_URL from "../api";
import { useEffect, useState } from "react";
import axios from "axios";

function MostHelpfulReviews() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`${API_URL}/api/most_helpful_reviews/`)
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching most helpful reviews:", error);
      });
  }, []);

  return (
    <section className="rounded-xl bg-white p-5 shadow-sm">
      <h2 className="mb-4 text-lg font-semibold text-gray-800">
        Most Helpful Reviews
      </h2>

      <div className="h-72 overflow-y-auto">
        <table className="w-full text-left">
          <thead className="sticky top-0 bg-white">
            <tr className="border-b border-gray-200 text-sm text-gray-500">
              <th className="px-3 py-2">Product</th>
              <th className="px-3 py-2">Score</th>
              <th className="px-3 py-2">Helpful</th>
            </tr>
          </thead>

          <tbody>
            {data.map((review) => (
              <tr
                key={review.id}
                className="border-b border-gray-100"
              >
                <td className="px-3 py-2 text-sm font-medium text-gray-800">
                  {review.product_id}
                </td>

                <td className="px-3 py-2 text-sm text-gray-600">
                  {review.score}
                </td>

                <td className="px-3 py-2 text-sm text-gray-600">
                  {review.helpfulness_numerator}/
                  {review.helpfulness_denominator}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default MostHelpfulReviews;