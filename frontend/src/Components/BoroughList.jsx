import React, {use, useEffect} from "react";
import { useGeoData } from "./GeoDataContext";

export default function BoroughList() {
  const { geoData, geoDataAreLoading, geoDataError, reloadGeoData } =
    useGeoData();

  if (geoDataAreLoading) return <p>Загрузка...</p>;
  if (geoDataError) return <p style={{ color: "red" }}>Ошибка: {geoDataError}</p>;

  console.log("Rendering BoroughList with geodata:", geoData);

  return (
    <div>
      <button onClick={reloadGeoData}>🔄 Обновить</button>
      <h1>Список районов</h1>
      {geoDataAreLoading && <p>Загрузка...</p>}
      {geoDataError && <p style={{ color: "red" }}>Ошибка: {geoDataError}</p>}
      {console.log("GeoData in render:", geoData)}

      <ul>
        {geoData.map((area) => (
          <li key={area.id}>
            <strong>{area.name}</strong>
            <ul>
              {area.boroughs?.map((b) => (
                <li key={b.id}>
                  {b.name} — {b.area}
                  {b.border && (
                    <pre
                      style={{
                        whiteSpace: "pre-wrap",
                        wordBreak: "break-all",
                        backgroundColor: "#f0f0f0",
                        padding: "5px",
                      }}
                    >
                      {JSON.stringify(b.border, null, 2)}
                    </pre>
                  )}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}
