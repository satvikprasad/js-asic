import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge

@cocotb.test()
async def counts_only_when_enabled(dut):
    cocotb.start_soon(Clock(dut.clk, 20, unit="ns").start())
    dut.rst.value, dut.en.value = 1, 0

    await FallingEdge(dut.clk); await FallingEdge(dut.clk)
    dut.rst.value = 0

    for expected in range(1, 6):
        dut.en.value = 1
        await FallingEdge(dut.clk)

        assert dut.count.value == expected

    dut.en.value = 0
    await FallingEdge(dut.clk)
    
    assert dut.count.value == 5
