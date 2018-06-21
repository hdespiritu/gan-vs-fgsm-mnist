def train_step(x_batch, y_batch):
                """
                A single training step
                """
                feed_dict = {
                  char_cnn.input_x: x_batch,
                  char_cnn.input_y: y_batch,
                  char_cnn.dropout_keep_prob: config.training.p
                }
                _, step, summaries, loss, accuracy, predictions, correct_predictions = sess.run(
                    [train_op,
                     global_step,
                     train_summary_op,
                     char_cnn.loss,
                     char_cnn.accuracy,
                     char_cnn.predictions,
                     char_cnn.correct_predictions],
                    feed_dict)

                #confusion matrix summaries

                img_d_summary_dir = os.path.join(out_dir, "summaries", "train")#"img")
                img_d_summary_writer = tf.summary.FileWriter(img_d_summary_dir, sess.graph)
                img_d_summary =  plot_confusion_matrix(predictions, y_batch, data_classes,  tensor_name='train/cm')
                img_d_summary_writer.add_summary(img_d_summary, step)
                                {}
                time_str = datetime.datetime.now().isoformat()
                print("{}: step {}, loss {:g}, acc {:g}".forstep)ime_str, step, loss, accuracy))
                #train_summary_writer.add_summary(tf.summary.merge([summaries, img_d_summary]), step)
                train_summary_writer.add_summary(summaries, 
            def dev_step(x_batch, y_batch, writer=None):
                """
                Evaluates model on a dev set
                """
                feed_dict = {
                  char_cnn.input_x: x_batch,
                  char_cnn.input_y: y_batch,
                  char_cnn.dropout_keep_prob: 1.0 # Disable dropout
                }
                step, summaries, loss, accuracy, predictions, correct_predictions = sess.run(
                    [global_step,
                     dev_summary_op,
                     char_cnn.loss,
                     char_cnn.accuracy,
                     char_cnn.predictions,
                     char_cnn.correct_predictions],
                    feed_dict)

                #confusion matrix summaries
                img_d_summary_dir = os.path.join(out_dir, "summaries", "dev")#"img")
                img_d_summary_writer = tf.summary.FileWriter(img_d_summary_dir, sess.graph)
                img_d_summary = plot_confusion_matrix(correct_predictions, predictions, data_classes, tensor_name='dev/cm')
                img_d_summary_writer.add_summary(img_d_summary, step)

                time_str = datetime.datetime.now().isoformat()

                print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
                if writer:
                    writer.add_summary(summaries, step)
                    #writer.add_summary(tf.summary.merge([summaries, img_d_summary]), step)
