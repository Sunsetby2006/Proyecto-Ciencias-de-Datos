import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Toplevel, ttk, messagebox, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AirbnbExploratoryAnalysis:
    def __init__(self, master):
        self.master = master
        self.df = self.load_data()
        self.setup_ui()
        self.show_data_summary()
        
    def load_data(self):
        """Carga y muestra información básica del dataset"""
        try:
            df = pd.read_csv("Base_de_datos.csv")
            
            # Mostrar información inicial en consola
            print("✅ Datos cargados exitosamente")
            print("\n🔍 Información inicial:")
            print(df.info())
            
            # Mostrar estadísticas descriptivas
            print("\n📊 Estadísticas descriptivas:")
            print(df.describe(include=[np.number]))  # Solo columnas numéricas
            
            return df
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{str(e)}")
            exit()

    def setup_ui(self):
        """Configura la interfaz gráfica"""
        self.master.title("Análisis Exploratorio Airbnb")
        self.master.geometry("500x600")
        
        # Marco principal
        main_frame = Frame(self.master)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        Label(main_frame, text="Análisis Exploratorio de Datos Airbnb", 
              font=("Arial", 14, "bold")).pack(pady=10)
        
        # Botones de análisis
        analyses = [
            ("1. Distribución de Precios", self.show_price_distribution),
            ("2. Precio por Tipo de Propiedad", self.show_price_by_property),
            ("3. Precio por Tipo de Habitación", self.show_price_by_room),
            ("4. Relación Precio-Características", self.show_price_relations),
            ("5. Mapa de Correlaciones Numéricas", self.show_numeric_correlations),
            ("6. Análisis Geográfico", self.show_geo_analysis),
            ("7. Análisis de Amenidades (Top 10)", self.show_top_amenities)
        ]
        
        for text, command in analyses:
            Button(main_frame, text=text, command=command, width=30).pack(pady=5)

    def show_data_summary(self):
        """Muestra información clave en la consola"""
        # Solo correlaciones numéricas para evitar el error
        numeric_cols = self.df.select_dtypes(include=[np.number])
        print("\n🔍 Variables numéricas más correlacionadas con el precio:")
        print(numeric_cols.corr()['log_price'].sort_values(ascending=False).head(5))
        
        print("\n📌 Valores nulos por columna:")
        print(self.df.isnull().sum())
        
        print("\n🏙️ Top 5 barrios con más propiedades:")
        print(self.df['neighbourhood'].value_counts().head(5))

    def create_plot_window(self, title, size=(1000, 600)):
        """Crea una ventana para visualización"""
        window = Toplevel(self.master)
        window.title(title)
        window.geometry(f"{size[0]}x{size[1]}")
        return window

    # Funciones de visualización
    def show_price_distribution(self):
        window = self.create_plot_window("Distribución de Precios")
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Histograma
        sns.histplot(self.df['log_price'], bins=30, kde=True, ax=axes[0])
        axes[0].set_title('Distribución de Precios (log)')
        axes[0].set_xlabel('Precio (log)')
        axes[0].set_ylabel('Frecuencia')
        
        # Boxplot
        sns.boxplot(x=self.df['log_price'], ax=axes[1])
        axes[1].set_title('Distribución de Precios')
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_price_by_property(self):
        window = self.create_plot_window("Precio por Tipo de Propiedad")
        
        # Filtrar solo los tipos de propiedad con suficientes datos
        top_properties = self.df['property_type'].value_counts().nlargest(10).index
        filtered_df = self.df[self.df['property_type'].isin(top_properties)]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(
            x='property_type', 
            y='log_price', 
            data=filtered_df,
            ax=ax,
            order=filtered_df.groupby('property_type')['log_price'].median().sort_values().index
        )
        ax.set_title('Distribución de Precios por Tipo de Propiedad (Top 10)')
        ax.set_xlabel('')
        ax.set_ylabel('Precio (log)')
        plt.xticks(rotation=45)
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_price_by_room(self):
        window = self.create_plot_window("Precio por Tipo de Habitación")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(
            x='room_type', 
            y='log_price', 
            data=self.df,
            ax=ax
        )
        ax.set_title('Distribución de Precios por Tipo de Habitación')
        ax.set_xlabel('')
        ax.set_ylabel('Precio (log)')
        plt.xticks(rotation=45)
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_price_relations(self):
        window = self.create_plot_window("Relación Precio-Características", (1200, 800))
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Relación con número de habitaciones
        sns.scatterplot(
            x='bedrooms',
            y='log_price',
            data=self.df,
            ax=axes[0, 0],
            alpha=0.6
        )
        axes[0, 0].set_title('Precio vs Dormitorios')
        
        # Relación con número de baños
        sns.scatterplot(
            x='bathrooms',
            y='log_price',
            data=self.df,
            ax=axes[0, 1],
            alpha=0.6
        )
        axes[0, 1].set_title('Precio vs Baños')
        
        # Relación con capacidad
        sns.scatterplot(
            x='accommodates',
            y='log_price',
            data=self.df,
            ax=axes[1, 0],
            alpha=0.6
        )
        axes[1, 0].set_title('Precio vs Capacidad')
        
        # Relación con evaluación
        sns.scatterplot(
            x='review_scores_rating',
            y='log_price',
            data=self.df,
            ax=axes[1, 1],
            alpha=0.6
        )
        axes[1, 1].set_title('Precio vs Evaluación')
        
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_numeric_correlations(self):
        window = self.create_plot_window("Correlaciones Numéricas", (900, 700))
        
        # Seleccionar solo columnas numéricas
        numeric_cols = self.df.select_dtypes(include=[np.number])
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        sns.heatmap(
            numeric_cols.corr(),
            annot=True,
            cmap="coolwarm",
            center=0,
            ax=ax,
            annot_kws={"size": 8}
        )
        ax.set_title('Mapa de Correlación entre Variables Numéricas')
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_geo_analysis(self):
        window = self.create_plot_window("Análisis Geográfico")
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        top_neighbourhoods = self.df['neighbourhood'].value_counts().nlargest(10).index
        filtered_df = self.df[self.df['neighbourhood'].isin(top_neighbourhoods)]
        
        scatter = sns.scatterplot(
            x='longitude',
            y='latitude',
            hue='log_price',
            size='log_price',
            data=filtered_df,
            alpha=0.6,
            palette='viridis',
            ax=ax
        )
        
        ax.set_title('Distribución Geográfica por Precio (Top 10 Barrios)')
        ax.set_xlabel('Longitud')
        ax.set_ylabel('Latitud')
        
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_top_amenities(self):
        window = self.create_plot_window("Amenidades Más Comunes")
        
        # Extraer y contar amenidades (asumiendo que están en una lista separada por comas)
        try:
            all_amenities = []
            for amenities_list in self.df['amenities'].dropna():
                # Limpiar y dividir las amenidades
                cleaned = amenities_list.replace('[', '').replace(']', '').replace('"', '')
                items = [item.strip() for item in cleaned.split(',') if item.strip()]
                all_amenities.extend(items)
            
            # Contar y obtener las 10 más comunes
            amenities_counts = pd.Series(all_amenities).value_counts().nlargest(10)
            
            fig, ax = plt.subplots(figsize=(12, 6))
            amenities_counts.plot(kind='barh', ax=ax, color='skyblue')
            ax.set_title('Top 10 Amenidades Más Comunes')
            ax.set_xlabel('Número de Propiedades')
            ax.invert_yaxis()  # Mostrar la más común arriba
            
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo analizar amenidades:\n{str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = AirbnbExploratoryAnalysis(root)
    root.mainloop()