import API_URL from "../api";
import { useEffect, useState } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function MonthlyReviewChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`${API_URL}/api/monthly_review_volume/`)
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching monthly review volume:", error);
      });
  }, []);

  return (
    <section className="mt-8 rounded-xl bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-xl font-semibold text-gray-800">
        Monthly Review Volume
      </h2>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="review_month" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="review_count"
              strokeWidth={2}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}

export default MonthlyReviewChart;