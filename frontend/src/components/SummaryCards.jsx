import API_URL from "../api";
import { useEffect, useState } from "react";
import axios from "axios";

function SummaryCards() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    axios
      .get(`${API_URL}/api/summary/`)
      .then((response) => {
        setSummary(response.data);
      })
      .catch((error) => {
        console.error("Error fetching summary:", error);
      });
  }, []);

  if (!summary) {
    return <p>Loading...</p>;
  }

  const cards = [
    {
      title: "Total Reviews",
      value: summary.total_reviews.toLocaleString(),
    },
    {
      title: "Total Products",
      value: summary.total_products.toLocaleString(),
    },
    {
      title: "Total Users",
      value: summary.total_users.toLocaleString(),
    },
    {
      title: "Average Score",
      value: summary.overall_avg_score,
    },
  ];

  return (
    <section>
      <h2 className="mb-4 text-xl font-semibold text-gray-800">
        Overview
      </h2>

      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {cards.map((card) => (
          <div
            key={card.title}
            className="rounded-xl bg-white p-6 shadow-sm"
          >
            <h3 className="text-sm font-medium text-gray-500">
              {card.title}
            </h3>

            <p className="mt-2 text-3xl font-bold text-gray-900">
              {card.value}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default SummaryCards;