module counter #(
    parameter W = 8
) (
    input clk,
    input rst,
    input en,
    output reg [W - 1 : 0] count,
    output wire wrap
);
  assign wrap = en && (count == {W{1'b1}});
  always @(posedge clk) begin
    if (rst) count <= 0;
    else if (en) count <= count + 1'b1;
  end
endmodule
