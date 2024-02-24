#include <gtk/gtk.h>
// Author VirgilRS
int current_image_index = 1;

void switch_image(GtkWidget *image) {
    char filename[10];
    sprintf(filename, "video/%d.jpg", current_image_index);
    gtk_image_set_from_file(GTK_IMAGE(image), filename);
    current_image_index = (current_image_index % 50) + 1; // Переход к следующей картинке (здесь 3 - это количество изображений в карусели)
}

int main( int argc, char *argv[] ) {
   GtkWidget *image;
   GtkWidget *window;
   gtk_init( &argc, &argv );
   
   window = gtk_window_new( GTK_WINDOW_TOPLEVEL ); // Создаем главное окно
   gtk_window_set_title( GTK_WINDOW( window ),  "Screensaver RS");
   image = gtk_image_new();
   gtk_window_fullscreen(GTK_WINDOW(window));   
   gtk_container_add( GTK_CONTAINER( window ), image ); 
   gtk_widget_show_all( window );

   g_timeout_add(25, (GSourceFunc)switch_image, image); // Автоматическая смена картинок каждые 2 секунды
   
   g_signal_connect( G_OBJECT( window ), "destroy", G_CALLBACK( gtk_main_quit ), NULL ); // Соединяем сигнал завершения с выходом
   gtk_main();
   return 0;
}
