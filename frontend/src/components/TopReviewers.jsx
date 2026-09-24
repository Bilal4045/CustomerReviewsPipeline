import API_URL from "../api";
import { useEffect, useState } from "react";
import axios from "axios";

function TopReviewers() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`${API_URL}/api/top_reviewers/`)
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching top reviewers:", error);
      });
  }, []);

  return (
    <section className="rounded-xl bg-white p-5 shadow-sm">
      <h2 className="mb-4 text-lg font-semibold text-gray-800">
        Top Reviewers
      </h2>

      <div className="h-72 overflow-y-auto">
        <table className="w-full text-left">
          <thead className="sticky top-0 bg-white">
            <tr className="border-b border-gray-200 text-sm text-gray-500">
              <th className="px-3 py-2">Reviewer</th>
              <th className="px-3 py-2">Reviews</th>
              <th className="px-3 py-2">Avg Score</th>
            </tr>
          </thead>

          <tbody>
            {data.map((reviewer) => (
              <tr
                key={reviewer.user_id}
                className="border-b border-gray-100"
              >
                <td className="px-3 py-2 text-sm font-medium text-gray-800">
                  {reviewer.profile_name || reviewer.user_id}
                </td>

                <td className="px-3 py-2 text-sm text-gray-600">
                  {reviewer.review_count.toLocaleString()}
                </td>

                <td className="px-3 py-2 text-sm text-gray-600">
                  {reviewer.avg_score_given}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default TopReviewers;